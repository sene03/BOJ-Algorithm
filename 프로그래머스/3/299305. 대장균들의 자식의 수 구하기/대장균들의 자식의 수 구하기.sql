select parent.id,
count(child.id) as CHILD_COUNT
from  ECOLI_DATA parent left join ECOLI_DATA child
on child.parent_id = parent.id
group by parent.id;
