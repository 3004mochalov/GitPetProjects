from tabulate import tabulate
import string
header = [('dec')]
list = string.printable
list2 = [('0','48'),('1','49'),('2','50'),('3','51'),('4','52'),('5','53'),('6','54'),('7','55'),('8','56'),('9','57'),(':','58')]
print(tabulate(list2, header, tablefmt="github"))



