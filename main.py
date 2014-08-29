#!/usr/bin/env python
import read_file
import parse_prop
import get_snpcount
import add_seq
import append
import integrate
import add_to_db
import run_struct
import get_sites

file = integrate.integrate()
df = read_file.read_file(file)
new_df = parse_prop.parse_prop(df)
#kage = get_snpcount.enough_info(file)
str = append.append(new_df)
sites, indices = get_sites.get_sites(new_df)
#add_to_db.add_to_base(kage,df)
run_struct.call_structure(sites, indices)




