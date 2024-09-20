MOUTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    #get date
    date = get_date()
    #print date
    print_date(date)


def get_date():
    while True:
        try:
            date = input('Date: ')
            date = format_date(date)
            if date:
                return date

        except EOFError:
            exit(0)
        
def format_date(date: str):
    #check if is formater and return format type 1 or 2
    splited_date = check_formated(date)
    if splited_date == False:
        return False
    #check if days in range 1-31
    elif check_days(splited_date) == False:
        return False
    #check if month in ranger
    elif check_month(splited_date)== False:
        return False
    else:
        return splited_date

def check_formated(date:str):
    """September 8, 1636 or 9/8/1636"""
    splited_date = date.split(sep= '/')
    if len(splited_date) == 3:
        return splited_date
    elif len(splited_date) == 1:
        splited_date = date.split(sep=' ')
        if len(splited_date) != 3: return False
        try:
            month = MOUTHS.index(splited_date[0]) + 1
        except ValueError:
            return False
        splited_date[0] = month
        splited_date[1] = splited_date[1][:-1]
        return splited_date

def check_days(date: list[str]):
    try: 
        day = int(date[1])
    except ValueError:
        return False
    
    if 0 < day <= 31:
        return True
    return False
    
def check_month(date: list[str]):
    try:
        month = int(date[0])
    except ValueError:
        return False
 
    if 0 < month <= 12:
        return True
    return False

def print_date(date: list[str]):
    print(f"{date[2]}-{int(date[1]):02}-{date[0]:02}")

if __name__ == '__main__':
    main()