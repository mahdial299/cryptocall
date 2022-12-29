
# Cryptocall

this was my first machine learning project which trys to predict cryptocurrency price in realtime mode


## Manual

After installing dependancies, lunch the console file in the terminal
then lunch datacrypto file another terminal, the default refresh rate is 1min
and in order to change the cryptocurrency type, you can change the crypt value (default_val : bitcoin)

```python 

crypt = 'bitcoin'
price = get_crypto(crypt)

```

the date value is the join value of month, day, hour and minute (year can be add at first)
which gives unique integer value as a feature


```python 

x_value = f'{e.month}{e.day}{e.hour}{e.minute}'

```

there is csv file which works as intermedian between console and data generator

in future developements this file can be delete (by use of Pipe() or Queue() module)
