# fuction for reading data and other fuctions 
import pandas as pd

#
def split_string_into_three_parts(s):
    ''' Splitt string three parts'''
    length = len(s)
    part_length = length // 3
    part1 = s[:part_length]
    part2 = s[part_length:2*part_length]
    part3 = s[2*part_length:]
    return part1, part2, part3

#
def read_data():
    excel_name = 'questionMistral_v01.xlsx'
    intoirscoreRangePy= 'IntoirScoreRangePy.xlsx'
    try:
        # Attempt to read the Excel file
        mistral_xlsx = pd.read_excel(excel_name, sheet_name='Mistral')
        scoreRangeDf = pd.read_excel(intoirscoreRangePy, sheet_name='ScoreRangePy')
        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except ValueError:
        print(f"Error: The file at {file_path} is not a valid Excel file or is corrupted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # select column filter some annoying words 
    mistral = mistral_xlsx[['Admin Reference','Construct','Order','likert_def','Likert Quantive','MckinseyManagerMistral', 'TenYearBoyMistral', 'VictorianWomanMistral','DrillSrgtMistral']] 
    #
    mistral['MckinseyManagerMistral'] = mistral['MckinseyManagerMistral'].str.replace('McKinsey Manager', '')
    mistral['MckinseyManagerMistral'] = mistral['MckinseyManagerMistral'].str.replace('McKinsey manager,', '')
    mistral['VictorianWomanMistral'] = mistral['VictorianWomanMistral'].str.replace('My dear', '')
    mistral['VictorianWomanMistral'] = mistral['VictorianWomanMistral'].str.replace('I must confess', '')
    mistral['DrillSrgtMistral'] = mistral['DrillSrgtMistral'].str.replace('Soldier', '')

    #
    leChat_first, leChat_middle, leChat_last  = split_string_into_three_parts(in_leChat)
    mistral['leChat'] = in_leChat
    mistral['leChat_first'] = leChat_first
    mistral['leChat_middle'] = leChat_middle
    mistral['leChat_last'] = leChat_last

    return mistral

    


