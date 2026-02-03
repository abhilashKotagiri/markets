# in simple terms, using risk parity function, we determine weightage for each asset class
# Ideally atleast 30 stocks are required for a diversified portfolio. So, we divide 30 * asset class weightage. which gives the  number of portions each 
# asset class budget needs to be divided into
#alternatively, if the number of stocks inputed by user per asset class is greater than the number previously determined, we use below logic
# to divide upon the each asset class budget.
# asset classes:
# l1 = large cap nifty50, l2 = large cap next 50, l3 = midcap, l4 = smallcap , l5 = microcap, l6 = nanocap


# better way for user input is needed, suc h as .csv file or a simple json or txt file. As they are just value pairs.

def risk_parity():


	final_weight = []
	total_inverse = 0

	vols = [0.15, 0.20,0.28,0.40,0.60,0.75]

	for m in vols:

		inverse_vol = 1/m
		total_inverse += inverse_vol

	for k in vols:
		final_weight.append(round((((1/k)/total_inverse)*100),2))
 
	return final_weight





# main function

portfolio_value = 356675
base_alloc = 1.5
max_alloc = 8
min_number_stocks = 30


list_of_data = [
	('tcs', 'l1'),
	('ccl', 'l4'),
	('asianpaint','l1'),
	('ASTRAL', 'l3'),
	('AEROENTER', 'l5'),
	('ARE&M', 'l4'),
	('BOROSCI', 'l5'),
	('COLPAL', 'l3'),
	('DYNPRO', 'l5'),
	('IEX', 'l4'),
	('INFY', 'l1'),
	('ITC', 'l1'),
	('KABRAEXTRU', 'l5'),
	('KAMOPAINTS', 'l5'),
	('KOTAKBANK', 'l1'),
	('NESTLEIND', 'l2'),
	('TMCV', 'l2'),
	('TMPV', 'l2'),
	('VIYASH', 'l6'),


]


list_of_data.sort(key=lambda data:data[1], reverse=True)


risk_parity_weights = risk_parity()

print(risk_parity_weights)
l1_weight, l2_weight, l3_weight, l4_weight, l5_weight, l6_weight = risk_parity_weights

l1_budget = round((l1_weight*portfolio_value)/100,2)
l2_budget = round((l2_weight*portfolio_value)/100,2)
l3_budget = round((l3_weight*portfolio_value)/100,2)
l4_budget = round((l4_weight*portfolio_value)/100,2)
l5_budget = round((l5_weight*portfolio_value)/100,2)
l6_budget = round((l6_weight*portfolio_value)/100,2)

print(l1_budget, l2_budget, l3_budget, l4_budget, l5_budget, l6_budget)

l1_count,l2_count,l3_count,l4_count,l5_count,l6_count =[0,0,0,0,0,0]


for a,b in list_of_data:

	if b == 'l1':
		l1_count +=1
	elif b == 'l2':
		l2_count +=1
	elif b == 'l3':
		l3_count +=1
	elif b == 'l4':
		l4_count +=1
	elif b == 'l5':
		l5_count +=1
	elif b == 'l6':
		l6_count +=1


for m,n in list_of_data:
	if n == 'l1':


		#if number of stocks mentioned by user per band are greater than minimum number of required stocks
		if l1_count> (min_number_stocks*(l1_weight/100)):
			l1_final_weight = (l1_budget/l1_count)

		else:

		#divides budget by minimum number of stocks to be allocated per band
			l1_final_weight = (l1_budget/(min_number_stocks*(l1_weight/100)))
			print(f"Allocation for {m} : {l1_final_weight}")

	elif n == 'l2':

		if l2_count> (min_number_stocks*(l2_weight/100)):
				l2_final_weight = (l2_budget/l2_count)

		else:

			l2_final_weight = (l2_budget/(min_number_stocks*(l2_weight/100)))
			print(f"Allocation for {m} : {l2_final_weight}")



	elif n == 'l3':

		if l3_count> (min_number_stocks*(l3_weight/100)):

			l3_final_weight = (l3_budget/l3_count)

		else:


			l3_final_weight = (l3_budget/(min_number_stocks*(l3_weight/100)))
			print(f"Allocation for {m} : {l3_final_weight}")

	elif n == 'l4':

		if l4_count> (min_number_stocks*(l4_weight/100)):
			l4_final_weight = (l4_budget/l4_count)

		else:


			l4_final_weight = (l4_budget/(min_number_stocks*(l4_weight/100)))
			print(f"Allocation for {m} : {l4_final_weight}")

	elif n == 'l5':

		if l5_count> (min_number_stocks*(l5_weight/100)):
			l5_final_weight = (l5_budget/l5_count)

		else:

			l5_final_weight = (l5_budget/(min_number_stocks*(l5_weight/100)))
			print(f"Allocation for {m} : {l5_final_weight}")

	else:
		#nano

		if l6_count> (min_number_stocks*(l6_weight/100)):
			l6_final_weight = (l6_budget/l6_count)
		
		else:

			l6_final_weight = (l6_budget/(min_number_stocks*(l6_weight/100)))
			print(f"Allocation for {m} : {l6_final_weight}")


			


