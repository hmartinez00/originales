import pandas as pd
from sync_voice_over.json_queries import dir_access, json_query, date_str, export

date = date_str()

# Exportar a csv
data = pd.DataFrame({
    'links'     : ['links'],
    'titles'    : ['titles'],
    'paragraphs': ['paragraphs'],
})
file = 'summary_' + date + '.xlsx'
export(data, file)