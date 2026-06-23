
  
    
    
    create  table main."customer_summary"
    as
        select
    count(*) as total_customers
from main."customers"

  