# fuction for reading data and other fuctions 
# intoir_Functions 
# 20240609
import pandas as pd
import warnings
import spacy
import numpy as np
import re
#import streamlit.components.v1 as components
#
nlp = spacy.load('en_core_web_sm')
warnings.filterwarnings("ignore") # Turn off all warnings
#
def compare_similarity(cv1_text, cv2_text):
    ''' Compare similarity '''
    cv1_doc = nlp(cv1_text)
    cv2_doc = nlp(cv2_text)
    similarity_score = cv1_doc.similarity(cv2_doc)
    return similarity_score
#    
def split_string_into_three_parts(s):
    ''' Splitt string three parts'''
    length = len(s)
    part_length = length // 3
    part1 = s[:part_length]
    part2 = s[part_length:2*part_length]
    part3 = s[2*part_length:]
    return part1, part2, part3
    
def make_html_recommendations (construct_score):
    ''' Need Construct, Rank Recommendations
    Return html'''
    df = construct_score [['Construct', 'Rank', 'Recommendations']]
    # Create HTML document
    html_doc = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    body {
      width: 50%;
      font-family: Arial, sans-serif;
    }
    .header {
      font-weight: bold;
    }
    </style>
    </head>
    <body>
    """

    for row in df.itertuples():
        html_doc += f"""
        <div>
          <span class='header'>{row.Construct}</span> - <span class='header'>{row.Rank}</span>
          <p>{row.Recommendations}</p>
        </div>
        """

    html_doc += """
    </body>
    </html>
    """
    return html_doc


#
def main_fx(in_leChat):
    excel_name = 'questionMistral_v01.xlsx'
    intoirscoreRangePy = 'IntoirScoreRangePy.xlsx'
    try:
        # Attempt to read the Excel file
        mistral_xlsx = pd.read_excel(excel_name, sheet_name='Mistral')
        #scoreRangeDf = pd.read_excel(intoirscoreRangePy, sheet_name='ScoreRangePy')
    except FileNotFoundError:
        print(f"Error: The file at was not found.")
    except ValueError:
        print(f"Error: The file at  is not a valid Excel file or is corrupted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    #
    scoreRangeDf = pd.read_excel(intoirscoreRangePy, sheet_name='ScoreRangePy')
    scoreRangeDf = scoreRangeDf.rename(columns=lambda x: x.strip())

    mistral = mistral_xlsx[['Admin Reference','Construct','Order','likert_def','Likert Quantive','MckinseyManagerMistral', 'TenYearBoyMistral', 'VictorianWomanMistral','DrillSrgtMistral']] 
    #
    mistral['MckinseyManagerMistral'] = mistral['MckinseyManagerMistral'].str.replace('McKinsey Manager', '')
    mistral['MckinseyManagerMistral'] = mistral['MckinseyManagerMistral'].str.replace('McKinsey manager,', '')
    mistral['VictorianWomanMistral'] = mistral['VictorianWomanMistral'].str.replace('My dear', '')
    mistral['VictorianWomanMistral'] = mistral['VictorianWomanMistral'].str.replace('I must confess', '')
    mistral['DrillSrgtMistral'] = mistral['DrillSrgtMistral'].str.replace('Soldier', '')

    leChat_first, leChat_middle, leChat_last  = split_string_into_three_parts(in_leChat)
    mistral['leChat'] = in_leChat
    mistral['leChat_first'] = leChat_first
    mistral['leChat_middle'] = leChat_middle
    mistral['leChat_last'] = leChat_last

    #Score mistral
    mistral_score = mistral
        
    mistral_score['MckinseyM_Score_full'] = mistral_score.apply(lambda row: compare_similarity(row['MckinseyManagerMistral'], row['leChat']), axis=1)
    mistral_score['MckinseyM_Score_first'] = mistral_score.apply(lambda row: compare_similarity(row['MckinseyManagerMistral'], row['leChat_first']), axis=1)
    mistral_score['MckinseyM_Score_meddle'] = mistral_score.apply(lambda row: compare_similarity(row['MckinseyManagerMistral'], row['leChat_middle']), axis=1)
    mistral_score['MckinseyM_Score_last'] = mistral_score.apply(lambda row: compare_similarity(row['MckinseyManagerMistral'], row['leChat_last']), axis=1)
    
    mistral_score['Boy_Score_full'] = mistral_score.apply(lambda row: compare_similarity(row['TenYearBoyMistral'], row['leChat']), axis=1)
    mistral_score['Boy_Score_first'] = mistral_score.apply(lambda row: compare_similarity(row['TenYearBoyMistral'], row['leChat_first']), axis=1)
    mistral_score['Boy_Score_meddle'] = mistral_score.apply(lambda row: compare_similarity(row['TenYearBoyMistral'], row['leChat_middle']), axis=1)
    mistral_score['Boy_Score_last'] = mistral_score.apply(lambda row: compare_similarity(row['TenYearBoyMistral'], row['leChat_last']), axis=1)
    
    mistral_score['Victorian_Score_full'] = mistral_score.apply(lambda row: compare_similarity(row['VictorianWomanMistral'], row['leChat']), axis=1)
    mistral_score['Victorian_Score_first'] = mistral_score.apply(lambda row: compare_similarity(row['VictorianWomanMistral'], row['leChat_first']), axis=1)
    mistral_score['Victorian_Score_meddle'] = mistral_score.apply(lambda row: compare_similarity(row['VictorianWomanMistral'], row['leChat_middle']), axis=1)
    mistral_score['Victorian_Score_last'] = mistral_score.apply(lambda row: compare_similarity(row['VictorianWomanMistral'], row['leChat_last']), axis=1)
    
    mistral_score['Sergeant_Score_full'] = mistral_score.apply(lambda row: compare_similarity(row['DrillSrgtMistral'], row['leChat']), axis=1)
    mistral_score['Sergeant_Score_first'] = mistral_score.apply(lambda row: compare_similarity(row['DrillSrgtMistral'], row['leChat_first']), axis=1)
    mistral_score['Sergeant_Score_meddle'] = mistral_score.apply(lambda row: compare_similarity(row['DrillSrgtMistral'], row['leChat_middle']), axis=1)
    mistral_score['Sergeant_Score_last'] = mistral_score.apply(lambda row: compare_similarity(row['DrillSrgtMistral'], row['leChat_last']), axis=1)
    
    # mistral_out
    mistral_out = mistral   # use orginal
    getavg = mistral_score.iloc[:, 13:13+16]
    #
    quantile_x1 = 0.20
    quantile_x2 = 0.80
    #
    mistral_out ['row_sum'] = getavg.sum(axis=1)
    mistral_out ['row_mean'] = getavg.mean(axis=1)
    mistral_out ['row_lowquantile'] = getavg.quantile(quantile_x1,axis=1)
    mistral_out ['row_highquantile'] = getavg.quantile(quantile_x2,axis=1)
    mistral_out ['row_std'] = getavg.std(axis=1)
    # 
    mistral_out = mistral_out [['Admin Reference','Construct','Order','likert_def','row_lowquantile','row_highquantile','Likert Quantive']]
    lowquantile = mistral_out[(mistral_out['Likert Quantive'] ==1)]
    lowquantile= lowquantile.drop(['row_highquantile','Likert Quantive'], axis=1)
    highquantile = mistral_out [['Admin Reference','row_highquantile','Likert Quantive']]
    highquantile = highquantile [(highquantile['Likert Quantive'] ==1)]
    highquantile = highquantile.drop('Likert Quantive', axis=1, )
    mistral_out = pd.merge(lowquantile, highquantile, on='Admin Reference', how='inner')
    mistral_out = pd.merge(lowquantile, highquantile, on='Admin Reference', how='inner')
    # Construct_ration
    mistral_out['Construct_ration'] = (mistral_out.row_highquantile / mistral_out.row_lowquantile)
    min_value = mistral_out['Construct_ration'].min()
    max_value = mistral_out['Construct_ration'].max()
    number_of_bins = 3
    bin_edges = np.linspace(min_value, max_value, number_of_bins + 1)

    # Generate bin labels
    bin_labels = range(1, number_of_bins + 1)

    # Step 4: Apply the bins to the DataFrame column
    mistral_out['BinnedOneToFive'] = pd.cut(mistral_out['Construct_ration'], bins=bin_edges, labels=bin_labels, include_lowest=True)
    mistral_out['BinnedOneToFive'] = mistral_out['BinnedOneToFive'].astype(int) +1
    mistral_out.loc [mistral_out.Construct_ration == mistral_out.Construct_ration.max (),'BinnedOneToFive' ] = 12
    mistral_out.loc [mistral_out.Construct_ration == mistral_out.Construct_ration.min (),'BinnedOneToFive' ] = 1
    #
    construct_score =  mistral_out.groupby('Construct')['BinnedOneToFive'].mean().reset_index(name='avg_BinnedOneToFive')
    # scoreRangeDf merge from excel 
    construct_score = pd.merge(construct_score, scoreRangeDf, on='Construct')
    construct_score = construct_score [(construct_score.avg_BinnedOneToFive >= construct_score.ScoreRangeStart) & 
            (construct_score.avg_BinnedOneToFive < construct_score.ScoreRangeStop)]
            
    # recommendations        
    construct_score['Rank'] =  round (construct_score.avg_BinnedOneToFive, 2)
    combined_textXX = construct_score [['Construct','Rank', 'Recommendations' ]]
    recommendations = '\n'.join(combined_textXX.astype(str).values.flatten())

    
    return recommendations, mistral_out, mistral_score, construct_score

    


