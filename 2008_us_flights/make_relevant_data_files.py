import json
import pandas as pd


def create_airport_coords():
	df = pd.read_csv('source_data/airports.txt', names=None, usecols=[4, 6, 7])
	
	ret_dict = {}
	for i in range(df.shape[0]):
		ret_dict[df.iloc[i, 0]] = [df.iloc[i, 1], df.iloc[i, 2]]
	 
	with open('data/airport_coords.json', 'w+') as fp:
		json.dump(ret_dict, fp)


def grouped_by_month_and_origin():
	df = pd.read_csv(
		'source_data/data.csv', 
		usecols=['Month', 'DayofMonth', 'DayOfWeek', 'Origin', 'DepDelay']
	)

	df = df.loc[df.notnull().all(axis=1), :]	
	grouped = df.groupby(['Month', 'Origin'])
	medians = grouped['DepDelay'].median().rename('median')
	pd_to_json = medians.reset_index()
	with open('data/medians_grouped_by_month_and_origin.json', 'w+') as fp:
		pd_to_json.to_json(fp, orient='records')


if __name__ == '__main__':
	create_airport_coords()
	grouped_by_month_and_origin()
