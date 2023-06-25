Bill  = float(input("What was the total bill amount?\n$"))
Percentage = int(input("What percentage tip would you like to give?\n"))
People = int(input("How many people to split the bill?\n"))

Bill_Total = (((((Percentage) / 100) * (Bill)) + (Bill)))

Total = (Bill_Total / People)

Output = (
  f"\nYour summary is as follows: \
  \nBill: ${Bill:.2f} \
  \nTip: {Percentage}% \
  \nBill Total including tip: ${Bill_Total:.2f} \
  \nPeople: {People} \
  \nTotal Split between {People} people: ${Total:.2f}"
)

print(Output)