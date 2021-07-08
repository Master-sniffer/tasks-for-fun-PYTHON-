import numpy as np
import pandas as pd
import datetime
import data_examples
import feature_engineering
import pipeline


class MeanDummyRegressor():
    def predict(self, x):
        return np.mean(x)


def predict_cao(charge_chemistry, limestone_consumptions,
                charge_consumptions, coke_consumptions,
                coke_sieving, limestone_cao):
    charge = pd.DataFrame(charge_chemistry)
    limestone_consumption = pd.DataFrame(
        limestone_consumptions)
    charge_consumptions = pd.DataFrame(
        charge_consumptions)
    concentrate_limestone_consumption = charge_consumptions.copy()
    charge_consumptions.columns = [
        'DATETIME',
        'concentrate_limestone_consumption']
    coke_percent = pd.DataFrame(coke_consumptions)
    Sieving3mm_fuel = pd.DataFrame(
        coke_sieving)
    CAO_limestone = pd.DataFrame(limestone_cao)
    params = {
        'limestone_consumption': limestone_consumption,
        'charge_consumption': charge_consumptions,
        'concentrate_limestone_consumption': concentrate_limestone_consumption,
        'coke_percent': coke_percent,
        'Sieving3mm_fuel': Sieving3mm_fuel,
        'CAO_limestone': CAO_limestone,
        'charge': charge, }
    for param in params:
        params[param].index = params[param]['DATETIME']
        params[param].sort_index(ascending=False)
        params[param].drop(columns=['DATETIME'], inplace=True)
    frequent_df = params['limestone_consumption']
    frequent_params = ['concentrate_limestone_consumption',
                       'charge_consumption', 'coke_percent']
    for param in frequent_params:
        frequent_df = pd.merge_asof(right=frequent_df.sort_index(),
                                    left=params[param].sort_index(),
                                    left_index=True,
                                    right_index=True,
                                    tolerance=pd.Timedelta('5m'),
                                    direction='nearest'
                                    )
    frequent_df.dropna(inplace=True)
    params_df = pd.DataFrame()
    params_df['Расход кокса'] = (frequent_df['charge_consumption'] *
                                 frequent_df['coke_percent'] * 0.01
                                 ).resample('60T').mean()
    params_df['Расход извести + концентрата'] = (
        frequent_df['concentrate_limestone_consumption'].resample('60T').mean()
        )
    params_df['Расход извести'] = (
        frequent_df[frequent_df.index.minute == 0]['limestone_consumption']
    )
    params_df['Расход концентрата'] = (
        params_df['Расход извести + концентрата'] -
        params_df['Расход извести'])
    params_df['Расход шихты '] = (
        params_df['Расход извести + концентрата']
        - params_df['Расход кокса'])
    params_df['Concentrate'] = (params_df['Расход концентрата'] /
                                params_df['Расход шихты '])
    columns_to_delete = ['Расход кокса', 'Расход извести + концентрата',
                         'Расход извести', 'Расход концентрата',
                         'Расход шихты ']
    params_df.drop(columns=columns_to_delete, inplace=True)
    charge_df = params['charge']
    params_df = pd.merge_asof(
        left=params_df.sort_index(),
        right=charge_df.sort_index(),
        left_index=True,
        right_index=True,
        tolerance=pd.Timedelta('30m'),
        direction='nearest',
    )
    params_df.dropna(inplace=True)
    sieveing_df = params['Sieving3mm_fuel']
    cao_limestone_df = params['CAO_limestone']
    date_time_list = (list(sieveing_df.index) + list(cao_limestone_df.index)
                      + list(params_df.index))
    time_indecies = [x for x in pd.date_range(
        min(date_time_list) - pd.Timedelta('1h'),
        max(date_time_list) + pd.Timedelta('1h'),
        freq='H')
                     ]
    temp_df = pd.DataFrame(data=np.zeros(len(time_indecies)),
                           index=time_indecies
                           )
    temp_df = temp_df.merge(sieveing_df,
                            left_index=True,
                            right_index=True,
                            how='outer'
                            )
    temp_df = temp_df.merge(cao_limestone_df,
                            left_index=True,
                            right_index=True,
                            how='outer'
                            )
    for col in temp_df.columns:
        temp_df[col] = temp_df[col].replace({0: None})
        temp_df[col] = temp_df[col].astype(float).interpolate()
    temp_df = temp_df.drop(columns=[0])
    params_df = pd.merge_asof(
        left=params_df,
        right=temp_df,
        left_index=True,
        right_index=True,
        tolerance=pd.Timedelta('30m'),
        direction='nearest',
    )
    params_df['DATETIME'] = params_df.index
    params_df.reset_index(drop=True, inplace=True)

    params_df = params_df.dropna()
    params_df = params_df.reset_index(drop=True)
    columns_rolling_4 = ['CAO_charge', 'Concentrate',
                         'OSN_charge', 'TIO2_charge',
                         'Sieving3mm_fuel'
                         ]
    columns_rolling_3 = []
    columns_rolling_2 = ['CAO_charge',
                         'CAO_limestone']
    rolls = [
        columns_rolling_2,
        columns_rolling_3,
        columns_rolling_4]
    params_df_with_rolling = params_df.copy()
    for number, rol in enumerate(rolls):
        for col in rol:
            try:
                params_df_with_rolling[[col + f"_rolling_{number + 2}"]] = (
                    params_df_with_rolling[[col]].rolling(number + 2).mean()
                )
            except (RuntimeError, TypeError, NameError):
                pass
    params_df_with_rolling = feature_engineering.filMet(params_df_with_rolling)
    features = feature_engineering.fitcha(params_df_with_rolling)
    model = MeanDummyRegressor()
    result = float(model.predict(features.iloc[1]))
    return result
