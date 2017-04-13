#coding=utf-8    
arrWeek = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];  
arrMonth = ["January","February","March","April","May","June","July","August","September","October","November","December"];  
  
def is_leap_year(year):  
    if (year % 4 ==0 and year % 100 !=0 or year % 400 ==0):  
        return True  
    else:  
        return False  
      
def get_month_days(year,month):  
        if(month in (1,3,5,7,8,10,12)):  
            return 31;  
        elif(month in (4,6,9,11)):  
            return 30;  
        elif(is_leap_year(year)):  
            return 29;  
        else:  
            return 28;  
def get_total_days(year,month):  
        days = 0;  
        for i in range(1800,year):  
            if(is_leap_year(i)):   
                days += 366;       
            else:  
                days += 365;       
          
        for j in range(1,month):  
            days += get_month_days(year, j);  
        return days;  
              
def get_start_day(year,month):  
        return (3 + get_total_days(year, month)) % 7;    
  
def print_calendar(year):     
    for k,m in enumerate(arrMonth):  
        print "    ",m,"   ",year                    
        print "---------------------------"  
          
        day = get_month_days(year, k+1);  
        startDay = get_start_day(year, k+1);          

        for k,v in enumerate(arrWeek):                
            print "%3s" % v,                      
        print  
          
        for i in range(1,day+1):  
            temp = (startDay + i-1) % 7       
            if(i==1):  
                for j in range(temp):                 
                    print "   ",  
            print "%3s" % i,  
            if(temp == 6) :                           
                print  
        print                                         
        print "---------------------------"  
  
print_calendar(2017);         
