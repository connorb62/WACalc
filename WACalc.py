# Weighted Average Calculator
# WACalc

test_score_1 = input('Enter Grade (1st): ')
test_score_2 = input('Enter Grade (2nd): ')
test_score_3 = input('Enter Grade (3rd): ')

weight_factor_1 = input('Enter Weight Factor (dec) (1st): ')
weight_factor_2 = input('Enter Weight Factor (dec) (2st): ')
weight_factor_3 = input('Enter Weight Factor (dec) (3st): ')

test_weight_1 = float(test_score_1) * float(weight_factor_1)
test_weight_2 = float(test_score_2) * float(weight_factor_2)
test_weight_3 = float(test_score_3) * float(weight_factor_3)

average = float(test_weight_1) + float(test_weight_2) + float(test_weight_3)
print('Weighted Average: ', average)

