# Import Report

This report was generated from `Expenses Export.csv` using the app import logic.


## Row 1: February rent
- Raw CSV: {'date': '01-02-2026', 'description': 'February rent', 'paid_by': 'Aisha', 'amount': '48000', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Meera', 'split_details': '', 'notes': ''}
- Parsed date: '01-02-2026' -> datetime.date(2026, 2, 1)
- Amount: 48000 INR -> 48000.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Meera']
- Split details: 
- Computed shares: {'Aisha': 12000.0, 'Rohan': 12000.0, 'Priya': 12000.0, 'Meera': 12000.0}
- Anomalies: none

## Row 2: Groceries BigBasket
- Raw CSV: {'date': '03-02-2026', 'description': 'Groceries BigBasket', 'paid_by': 'Priya', 'amount': '2340', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Meera', 'split_details': '', 'notes': ''}
- Parsed date: '03-02-2026' -> datetime.date(2026, 2, 3)
- Amount: 2340 INR -> 2340.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Meera']
- Split details: 
- Computed shares: {'Aisha': 585.0, 'Rohan': 585.0, 'Priya': 585.0, 'Meera': 585.0}
- Anomalies: none

## Row 3: Wifi bill Feb
- Raw CSV: {'date': '05-02-2026', 'description': 'Wifi bill Feb', 'paid_by': 'Rohan', 'amount': '1199', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Meera', 'split_details': '', 'notes': ''}
- Parsed date: '05-02-2026' -> datetime.date(2026, 2, 5)
- Amount: 1199 INR -> 1199.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Meera']
- Split details: 
- Computed shares: {'Aisha': 299.75, 'Rohan': 299.75, 'Priya': 299.75, 'Meera': 299.75}
- Anomalies: none

## Row 4: Dinner at Marina Bites
- Raw CSV: {'date': '08-02-2026', 'description': 'Dinner at Marina Bites', 'paid_by': 'Dev', 'amount': '3200', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Dev', 'split_details': '', 'notes': 'Dev visiting for the weekend'}
- Parsed date: '08-02-2026' -> datetime.date(2026, 2, 8)
- Amount: 3200 INR -> 3200.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Dev']
- Split details: 
- Computed shares: {'Aisha': 800.0, 'Rohan': 800.0, 'Priya': 800.0, 'Dev': 800.0}
- Anomalies: none

## Row 5: dinner - marina bites
- Raw CSV: {'date': '08-02-2026', 'description': 'dinner - marina bites', 'paid_by': 'Dev', 'amount': '3200', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Dev', 'split_details': '', 'notes': ''}
- Parsed date: '08-02-2026' -> datetime.date(2026, 2, 8)
- Amount: 3200 INR -> 3200.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Dev']
- Split details: 
- Computed shares: {'Aisha': 800.0, 'Rohan': 800.0, 'Priya': 800.0, 'Dev': 800.0}
- Anomalies: none

## Row 6: Electricity Feb
- Raw CSV: {'date': '10-02-2026', 'description': 'Electricity Feb', 'paid_by': 'Aisha', 'amount': '1,200', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Meera', 'split_details': '', 'notes': ''}
- Parsed date: '10-02-2026' -> datetime.date(2026, 2, 10)
- Amount: 1,200 INR -> 1200.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Meera']
- Split details: 
- Computed shares: {'Aisha': 300.0, 'Rohan': 300.0, 'Priya': 300.0, 'Meera': 300.0}
- Anomalies: none

## Row 7: Maid salary Feb
- Raw CSV: {'date': '12-02-2026', 'description': 'Maid salary Feb', 'paid_by': 'Meera', 'amount': '3000', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Meera', 'split_details': '', 'notes': ''}
- Parsed date: '12-02-2026' -> datetime.date(2026, 2, 12)
- Amount: 3000 INR -> 3000.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Meera']
- Split details: 
- Computed shares: {'Aisha': 750.0, 'Rohan': 750.0, 'Priya': 750.0, 'Meera': 750.0}
- Anomalies: none

## Row 8: Movie night snacks
- Raw CSV: {'date': '14-02-2026', 'description': 'Movie night snacks', 'paid_by': 'priya', 'amount': '640', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya', 'split_details': '', 'notes': 'Meera skipped'}
- Parsed date: '14-02-2026' -> datetime.date(2026, 2, 14)
- Amount: 640 INR -> 640.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya']
- Split details: 
- Computed shares: {'Aisha': 213.33, 'Rohan': 213.33, 'Priya': 213.33}
- Anomalies: none

## Row 9: Cylinder refill
- Raw CSV: {'date': '15-02-2026', 'description': 'Cylinder refill', 'paid_by': 'Rohan', 'amount': '899.995', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Meera', 'split_details': '', 'notes': ''}
- Parsed date: '15-02-2026' -> datetime.date(2026, 2, 15)
- Amount: 899.995 INR -> 899.995 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Meera']
- Split details: 
- Computed shares: {'Aisha': 225.0, 'Rohan': 225.0, 'Priya': 225.0, 'Meera': 225.0}
- Anomalies: none

## Row 10: Groceries DMart
- Raw CSV: {'date': '18-02-2026', 'description': 'Groceries DMart', 'paid_by': 'Priya S', 'amount': '1875', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Meera', 'split_details': '', 'notes': ''}
- Parsed date: '18-02-2026' -> datetime.date(2026, 2, 18)
- Amount: 1875 INR -> 1875.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Meera']
- Split details: 
- Computed shares: {'Aisha': 468.75, 'Rohan': 468.75, 'Priya': 468.75, 'Meera': 468.75}
- Anomalies: none

## Row 11: Aisha birthday cake
- Raw CSV: {'date': '20-02-2026', 'description': 'Aisha birthday cake', 'paid_by': 'Rohan', 'amount': '1500', 'currency': 'INR', 'split_type': 'unequal', 'split_with': 'Rohan;Priya;Meera', 'split_details': 'Rohan 700; Priya 400; Meera 400', 'notes': 'Aisha not charged obviously'}
- Parsed date: '20-02-2026' -> datetime.date(2026, 2, 20)
- Amount: 1500 INR -> 1500.0 in INR
- Split type: unequal
- Participants: ['Rohan', 'Priya', 'Meera']
- Split details: Rohan 700; Priya 400; Meera 400
- Computed shares: {'Rohan': 700.0, 'Priya': 400.0, 'Meera': 400.0}
- Anomalies: none

## Row 12: House cleaning supplies
- Raw CSV: {'date': '22-02-2026', 'description': 'House cleaning supplies', 'paid_by': '', 'amount': '780', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Meera', 'split_details': '', 'notes': "can't remember who paid"}
- Parsed date: '22-02-2026' -> datetime.date(2026, 2, 22)
- Amount: 780 INR -> 780.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Meera']
- Split details: 
- Computed shares: {'Aisha': 195.0, 'Rohan': 195.0, 'Priya': 195.0, 'Meera': 195.0}
- Anomalies:
  - Missing paid_by/payer value

## Row 13: Rohan paid Aisha back
- Raw CSV: {'date': '25-02-2026', 'description': 'Rohan paid Aisha back', 'paid_by': 'Rohan', 'amount': '5000', 'currency': 'INR', 'split_type': '', 'split_with': 'Aisha', 'split_details': '', 'notes': 'this is a settlement not an expense??'}
- Parsed date: '25-02-2026' -> datetime.date(2026, 2, 25)
- Amount: 5000 INR -> 5000.0 in INR
- Split type: settlement
- Participants: ['Aisha']
- Split details: 
- Computed shares: {'Aisha': 0.0}
- Anomalies:
  - Treated as settlement because split_type is blank and one payee is listed
- Parser errors: ['Unsupported split type settlement']

## Row 14: Pizza Friday
- Raw CSV: {'date': '28-02-2026', 'description': 'Pizza Friday', 'paid_by': 'Aisha', 'amount': '1440', 'currency': 'INR', 'split_type': 'percentage', 'split_with': 'Aisha;Rohan;Priya;Meera', 'split_details': 'Aisha 30%; Rohan 30%; Priya 30%; Meera 20%', 'notes': 'percentages might be off'}
- Parsed date: '28-02-2026' -> datetime.date(2026, 2, 28)
- Amount: 1440 INR -> 1440.0 in INR
- Split type: percentage
- Participants: ['Aisha', 'Rohan', 'Priya', 'Meera']
- Split details: Aisha 30%; Rohan 30%; Priya 30%; Meera 20%
- Computed shares: {'Aisha': 432.0, 'Rohan': 432.0, 'Priya': 432.0, 'Meera': 288.0}
- Anomalies:
  - Percentage split details may be invalid
- Parser errors: ['Percentages do not sum to 100 (110.0%)']

## Row 15: March rent
- Raw CSV: {'date': '01-03-2026', 'description': 'March rent', 'paid_by': 'Aisha', 'amount': '48000', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Meera', 'split_details': '', 'notes': ''}
- Parsed date: '01-03-2026' -> datetime.date(2026, 3, 1)
- Amount: 48000 INR -> 48000.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Meera']
- Split details: 
- Computed shares: {'Aisha': 12000.0, 'Rohan': 12000.0, 'Priya': 12000.0, 'Meera': 12000.0}
- Anomalies: none

## Row 16: Groceries BigBasket
- Raw CSV: {'date': '03-03-2026', 'description': 'Groceries BigBasket', 'paid_by': 'Meera', 'amount': '2810', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Meera', 'split_details': '', 'notes': ''}
- Parsed date: '03-03-2026' -> datetime.date(2026, 3, 3)
- Amount: 2810 INR -> 2810.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Meera']
- Split details: 
- Computed shares: {'Aisha': 702.5, 'Rohan': 702.5, 'Priya': 702.5, 'Meera': 702.5}
- Anomalies: none

## Row 17: Wifi bill Mar
- Raw CSV: {'date': '05-03-2026', 'description': 'Wifi bill Mar', 'paid_by': 'Rohan', 'amount': '1199', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Meera', 'split_details': '', 'notes': ''}
- Parsed date: '05-03-2026' -> datetime.date(2026, 3, 5)
- Amount: 1199 INR -> 1199.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Meera']
- Split details: 
- Computed shares: {'Aisha': 299.75, 'Rohan': 299.75, 'Priya': 299.75, 'Meera': 299.75}
- Anomalies: none

## Row 18: Goa flights
- Raw CSV: {'date': '08-03-2026', 'description': 'Goa flights', 'paid_by': 'Aisha', 'amount': '32400', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Dev', 'split_details': '', 'notes': 'trip starts!'}
- Parsed date: '08-03-2026' -> datetime.date(2026, 3, 8)
- Amount: 32400 INR -> 32400.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Dev']
- Split details: 
- Computed shares: {'Aisha': 8100.0, 'Rohan': 8100.0, 'Priya': 8100.0, 'Dev': 8100.0}
- Anomalies: none

## Row 19: Goa villa booking
- Raw CSV: {'date': '09-03-2026', 'description': 'Goa villa booking', 'paid_by': 'Dev', 'amount': '540', 'currency': 'USD', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Dev', 'split_details': '', 'notes': 'booked on intl site'}
- Parsed date: '09-03-2026' -> datetime.date(2026, 3, 9)
- Amount: 540 USD -> 540.0 in USD
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Dev']
- Split details: 
- Computed shares: {'Aisha': 11205.0, 'Rohan': 11205.0, 'Priya': 11205.0, 'Dev': 11205.0}
- Anomalies: none

## Row 20: Beach shack lunch
- Raw CSV: {'date': '10-03-2026', 'description': 'Beach shack lunch', 'paid_by': 'Rohan', 'amount': '84', 'currency': 'USD', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Dev', 'split_details': '', 'notes': ''}
- Parsed date: '10-03-2026' -> datetime.date(2026, 3, 10)
- Amount: 84 USD -> 84.0 in USD
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Dev']
- Split details: 
- Computed shares: {'Aisha': 1743.0, 'Rohan': 1743.0, 'Priya': 1743.0, 'Dev': 1743.0}
- Anomalies: none

## Row 21: Scooter rentals
- Raw CSV: {'date': '10-03-2026', 'description': 'Scooter rentals', 'paid_by': 'Priya', 'amount': '3600', 'currency': 'INR', 'split_type': 'share', 'split_with': 'Aisha;Rohan;Priya;Dev', 'split_details': 'Aisha 1; Rohan 2; Priya 1; Dev 2', 'notes': 'Rohan and Dev took the bigger ones'}
- Parsed date: '10-03-2026' -> datetime.date(2026, 3, 10)
- Amount: 3600 INR -> 3600.0 in INR
- Split type: share
- Participants: ['Aisha', 'Rohan', 'Priya', 'Dev']
- Split details: Aisha 1; Rohan 2; Priya 1; Dev 2
- Computed shares: {'Aisha': 600.0, 'Rohan': 1200.0, 'Priya': 600.0, 'Dev': 1200.0}
- Anomalies: none

## Row 22: Parasailing
- Raw CSV: {'date': '11-03-2026', 'description': 'Parasailing', 'paid_by': 'Dev', 'amount': '150', 'currency': 'USD', 'split_type': 'equal', 'split_with': "Aisha;Rohan;Priya;Dev;Dev's friend Kabir", 'split_details': '', 'notes': 'Kabir joined for the day'}
- Parsed date: '11-03-2026' -> datetime.date(2026, 3, 11)
- Amount: 150 USD -> 150.0 in USD
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Dev', "Dev'S Friend Kabir"]
- Split details: 
- Computed shares: {'Aisha': 2490.0, 'Rohan': 2490.0, 'Priya': 2490.0, 'Dev': 2490.0, "Dev'S Friend Kabir": 2490.0}
- Anomalies: none

## Row 23: Dinner at Thalassa
- Raw CSV: {'date': '11-03-2026', 'description': 'Dinner at Thalassa', 'paid_by': 'Aisha', 'amount': '2400', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Dev', 'split_details': '', 'notes': ''}
- Parsed date: '11-03-2026' -> datetime.date(2026, 3, 11)
- Amount: 2400 INR -> 2400.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Dev']
- Split details: 
- Computed shares: {'Aisha': 600.0, 'Rohan': 600.0, 'Priya': 600.0, 'Dev': 600.0}
- Anomalies: none

## Row 24: Thalassa dinner
- Raw CSV: {'date': '11-03-2026', 'description': 'Thalassa dinner', 'paid_by': 'Rohan', 'amount': '2450', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Dev', 'split_details': '', 'notes': 'Aisha also logged this I think hers is wrong'}
- Parsed date: '11-03-2026' -> datetime.date(2026, 3, 11)
- Amount: 2450 INR -> 2450.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Dev']
- Split details: 
- Computed shares: {'Aisha': 612.5, 'Rohan': 612.5, 'Priya': 612.5, 'Dev': 612.5}
- Anomalies: none

## Row 25: Parasailing refund
- Raw CSV: {'date': '12-03-2026', 'description': 'Parasailing refund', 'paid_by': 'Dev', 'amount': '-30', 'currency': 'USD', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Dev', 'split_details': '', 'notes': 'one slot got cancelled'}
- Parsed date: '12-03-2026' -> datetime.date(2026, 3, 12)
- Amount: -30 USD -> -30.0 in USD
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Dev']
- Split details: 
- Computed shares: {'Aisha': -622.5, 'Rohan': -622.5, 'Priya': -622.5, 'Dev': -622.5}
- Anomalies: none

## Row 26: Airport cab
- Raw CSV: {'date': 'Mar-14', 'description': 'Airport cab', 'paid_by': 'rohan ', 'amount': '1100', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Dev', 'split_details': '', 'notes': ''}
- Parsed date: 'Mar-14' -> datetime.date(2026, 3, 14)
- Amount: 1100 INR -> 1100.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Dev']
- Split details: 
- Computed shares: {'Aisha': 275.0, 'Rohan': 275.0, 'Priya': 275.0, 'Dev': 275.0}
- Anomalies: none

## Row 27: Groceries DMart
- Raw CSV: {'date': '15-03-2026', 'description': 'Groceries DMart', 'paid_by': 'Priya', 'amount': '2105', 'currency': '', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Meera', 'split_details': '', 'notes': 'forgot to set currency'}
- Parsed date: '15-03-2026' -> datetime.date(2026, 3, 15)
- Amount: 2105 INR -> 2105.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Meera']
- Split details: 
- Computed shares: {'Aisha': 526.25, 'Rohan': 526.25, 'Priya': 526.25, 'Meera': 526.25}
- Anomalies:
  - Currency blank

## Row 28: Electricity Mar
- Raw CSV: {'date': '18-03-2026', 'description': 'Electricity Mar', 'paid_by': 'Aisha', 'amount': '1450', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Meera', 'split_details': '', 'notes': ''}
- Parsed date: '18-03-2026' -> datetime.date(2026, 3, 18)
- Amount: 1450 INR -> 1450.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Meera']
- Split details: 
- Computed shares: {'Aisha': 362.5, 'Rohan': 362.5, 'Priya': 362.5, 'Meera': 362.5}
- Anomalies: none

## Row 29: Maid salary Mar
- Raw CSV: {'date': '20-03-2026', 'description': 'Maid salary Mar', 'paid_by': 'Meera', 'amount': '3000', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Meera', 'split_details': '', 'notes': ''}
- Parsed date: '20-03-2026' -> datetime.date(2026, 3, 20)
- Amount: 3000 INR -> 3000.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Meera']
- Split details: 
- Computed shares: {'Aisha': 750.0, 'Rohan': 750.0, 'Priya': 750.0, 'Meera': 750.0}
- Anomalies: none

## Row 30: Dinner order Swiggy
- Raw CSV: {'date': '22-03-2026', 'description': 'Dinner order Swiggy', 'paid_by': 'Priya', 'amount': '0', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Meera', 'split_details': '', 'notes': 'counted twice earlier - fixing later'}
- Parsed date: '22-03-2026' -> datetime.date(2026, 3, 22)
- Amount: 0 INR -> 0.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Meera']
- Split details: 
- Computed shares: {'Aisha': 0.0, 'Rohan': 0.0, 'Priya': 0.0, 'Meera': 0.0}
- Anomalies: none

## Row 31: Weekend brunch
- Raw CSV: {'date': '25-03-2026', 'description': 'Weekend brunch', 'paid_by': 'Meera', 'amount': '2200', 'currency': 'INR', 'split_type': 'percentage', 'split_with': 'Aisha;Rohan;Priya;Meera', 'split_details': 'Aisha 30%; Rohan 30%; Priya 30%; Meera 20%', 'notes': ''}
- Parsed date: '25-03-2026' -> datetime.date(2026, 3, 25)
- Amount: 2200 INR -> 2200.0 in INR
- Split type: percentage
- Participants: ['Aisha', 'Rohan', 'Priya', 'Meera']
- Split details: Aisha 30%; Rohan 30%; Priya 30%; Meera 20%
- Computed shares: {'Aisha': 660.0, 'Rohan': 660.0, 'Priya': 660.0, 'Meera': 440.0}
- Anomalies:
  - Percentage split details may be invalid
- Parser errors: ['Percentages do not sum to 100 (110.0%)']

## Row 32: Meera farewell dinner
- Raw CSV: {'date': '28-03-2026', 'description': 'Meera farewell dinner', 'paid_by': 'Aisha', 'amount': '4800', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Meera', 'split_details': '', 'notes': 'Meera moving out Sunday :('}
- Parsed date: '28-03-2026' -> datetime.date(2026, 3, 28)
- Amount: 4800 INR -> 4800.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Meera']
- Split details: 
- Computed shares: {'Aisha': 1200.0, 'Rohan': 1200.0, 'Priya': 1200.0, 'Meera': 1200.0}
- Anomalies: none

## Row 33: Deep cleaning service
- Raw CSV: {'date': '04-05-2026', 'description': 'Deep cleaning service', 'paid_by': 'Rohan', 'amount': '2500', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya', 'split_details': '', 'notes': 'is this April 5 or May 4? format is a mess'}
- Parsed date: '04-05-2026' -> datetime.date(2026, 5, 4)
- Amount: 2500 INR -> 2500.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya']
- Split details: 
- Computed shares: {'Aisha': 833.33, 'Rohan': 833.33, 'Priya': 833.33}
- Anomalies: none

## Row 34: April rent
- Raw CSV: {'date': '01-04-2026', 'description': 'April rent', 'paid_by': 'Aisha', 'amount': '48000', 'currency': 'INR', 'split_type': 'share', 'split_with': 'Aisha;Rohan;Priya', 'split_details': 'Aisha 2; Rohan 1; Priya 1', 'notes': "Aisha took Meera's room too"}
- Parsed date: '01-04-2026' -> datetime.date(2026, 4, 1)
- Amount: 48000 INR -> 48000.0 in INR
- Split type: share
- Participants: ['Aisha', 'Rohan', 'Priya']
- Split details: Aisha 2; Rohan 1; Priya 1
- Computed shares: {'Aisha': 24000.0, 'Rohan': 12000.0, 'Priya': 12000.0}
- Anomalies: none

## Row 35: Groceries BigBasket
- Raw CSV: {'date': '02-04-2026', 'description': 'Groceries BigBasket', 'paid_by': 'Priya', 'amount': '2640', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Meera', 'split_details': '', 'notes': 'oops Meera still in the group list'}
- Parsed date: '02-04-2026' -> datetime.date(2026, 4, 2)
- Amount: 2640 INR -> 2640.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Meera']
- Split details: 
- Computed shares: {'Aisha': 660.0, 'Rohan': 660.0, 'Priya': 660.0, 'Meera': 660.0}
- Anomalies: none

## Row 36: Wifi bill Apr
- Raw CSV: {'date': '05-04-2026', 'description': 'Wifi bill Apr', 'paid_by': 'Rohan', 'amount': '1199', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya', 'split_details': '', 'notes': ''}
- Parsed date: '05-04-2026' -> datetime.date(2026, 4, 5)
- Amount: 1199 INR -> 1199.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya']
- Split details: 
- Computed shares: {'Aisha': 399.67, 'Rohan': 399.67, 'Priya': 399.67}
- Anomalies: none

## Row 37: Sam deposit share
- Raw CSV: {'date': '08-04-2026', 'description': 'Sam deposit share', 'paid_by': 'Sam', 'amount': '15000', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha', 'split_details': '', 'notes': 'Sam moving in! paid Aisha his deposit'}
- Parsed date: '08-04-2026' -> datetime.date(2026, 4, 8)
- Amount: 15000 INR -> 15000.0 in INR
- Split type: equal
- Participants: ['Aisha']
- Split details: 
- Computed shares: {'Aisha': 15000.0}
- Anomalies: none

## Row 38: Housewarming drinks
- Raw CSV: {'date': '10-04-2026', 'description': 'Housewarming drinks', 'paid_by': 'Sam', 'amount': '3100', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Sam', 'split_details': '', 'notes': ''}
- Parsed date: '10-04-2026' -> datetime.date(2026, 4, 10)
- Amount: 3100 INR -> 3100.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Sam']
- Split details: 
- Computed shares: {'Aisha': 775.0, 'Rohan': 775.0, 'Priya': 775.0, 'Sam': 775.0}
- Anomalies: none

## Row 39: Electricity Apr
- Raw CSV: {'date': '12-04-2026', 'description': 'Electricity Apr', 'paid_by': 'Aisha', 'amount': '1380', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Sam', 'split_details': '', 'notes': ''}
- Parsed date: '12-04-2026' -> datetime.date(2026, 4, 12)
- Amount: 1380 INR -> 1380.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Sam']
- Split details: 
- Computed shares: {'Aisha': 345.0, 'Rohan': 345.0, 'Priya': 345.0, 'Sam': 345.0}
- Anomalies: none

## Row 40: Groceries DMart
- Raw CSV: {'date': '15-04-2026', 'description': 'Groceries DMart', 'paid_by': 'Sam', 'amount': '1990', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Sam', 'split_details': '', 'notes': ''}
- Parsed date: '15-04-2026' -> datetime.date(2026, 4, 15)
- Amount: 1990 INR -> 1990.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Sam']
- Split details: 
- Computed shares: {'Aisha': 497.5, 'Rohan': 497.5, 'Priya': 497.5, 'Sam': 497.5}
- Anomalies: none

## Row 41: Furniture for common room
- Raw CSV: {'date': '18-04-2026', 'description': 'Furniture for common room', 'paid_by': 'Aisha', 'amount': '12000', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Sam', 'split_details': 'Aisha 1; Rohan 1; Priya 1; Sam 1', 'notes': 'split_type says equal but someone added shares anyway'}
- Parsed date: '18-04-2026' -> datetime.date(2026, 4, 18)
- Amount: 12000 INR -> 12000.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Sam']
- Split details: Aisha 1; Rohan 1; Priya 1; Sam 1
- Computed shares: {'Aisha': 3000.0, 'Rohan': 3000.0, 'Priya': 3000.0, 'Sam': 3000.0}
- Anomalies: none

## Row 42: Maid salary Apr
- Raw CSV: {'date': '20-04-2026', 'description': 'Maid salary Apr', 'paid_by': 'Priya', 'amount': '3000', 'currency': 'INR', 'split_type': 'equal', 'split_with': 'Aisha;Rohan;Priya;Sam', 'split_details': '', 'notes': ''}
- Parsed date: '20-04-2026' -> datetime.date(2026, 4, 20)
- Amount: 3000 INR -> 3000.0 in INR
- Split type: equal
- Participants: ['Aisha', 'Rohan', 'Priya', 'Sam']
- Split details: 
- Computed shares: {'Aisha': 750.0, 'Rohan': 750.0, 'Priya': 750.0, 'Sam': 750.0}
- Anomalies: none
