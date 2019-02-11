# santa-is-coming-2
A simple lottery program used to let me exchange (Christmas) gifts with friends

## Usage

- Change sender email to your own gmail in line 37 and 38

``` python
  gmail_user = 'yourgmail@gmail.com'
  gmail_password = 'yourgmailpassword'
```

- Create a csv (e.g. `test.csv`) with fields: `name`, `receipent`, `address`, `phone`, `wants` and `email`. 

``` csv
name,receipent,address,phone,wants,email
name1,receipent1,addredd1,phone1,wants1,yourmail+1@gmail.com
name2,receipent2,addredd2,phone2,wants2,yourmail+2@gmail.com
name3,receipent3,addredd3,phone3,wants3,yourmail+3@gmail.com
name4,receipent4,addredd4,phone4,wants4,yourmail+4@gmail.com
name5,receipent5,addredd5,phone5,wants5,yourmail+5@gmail.com
```

- Run it

``` bash
python3 lottery.py test.csv
```

- This program will shuffle the list and write to a output `test.csv.out`

``` csv
name,receipent,address,phone,wants,email
name4,receipent4,addredd4,phone4,wants4,yourmail+4@gmail.com
name3,receipent3,addredd3,phone3,wants3,yourmail+3@gmail.com
name1,receipent1,addredd1,phone1,wants1,yourmail+1@gmail.com
name2,receipent2,addredd2,phone2,wants2,yourmail+2@gmail.com
name5,receipent5,addredd5,phone5,wants5,yourmail+5@gmail.com
```

- It will send everyone in the list who and where they should send their gift to.
- Even the one runs this program won't know the results! (unless they check their sent box)