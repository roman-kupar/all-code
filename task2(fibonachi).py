def line (current, previous, sum):
    print(("Current Number %d Previous Number %d Sum %d") % (current , previous , sum))
     # Чому потрібно присвоювати значення, а не зразу виводи принтом з функції?
current = 0
previous = 0
for total in range(0, 20):
    line(current,previous,current+previous) 
    current += 1
    previous = current - 1
    #напевно можна було це все грамотніше написати)