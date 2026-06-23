select
    count(*) as total_customers
from {{ ref('customers') }}