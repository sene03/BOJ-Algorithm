select child.id as ID, child.genotype as GENOTYPE, parent.genotype as parent_genotype from ecoli_data child
join ecoli_data parent on child.parent_id = parent.id
where (parent.genotype & child.genotype) = parent.genotype
order by ID;