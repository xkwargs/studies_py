counter = 1
cumulator = 1

while counter <= 10:
    print(counter, cumulator)

    if counter > 5:
        break # Break sends the counter OUT of the while/else loop. Else will never be executed in this case.

    cumulator = cumulator + counter
    counter += 1
else:
    print('Finished in else')
print('Finished after else')