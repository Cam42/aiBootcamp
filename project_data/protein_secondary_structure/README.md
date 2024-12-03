
Downloaded 15,000 cif files with protein data out of the 227933 total from the rcsb protein database (https://www.rcsb.org/).  Only 15,000 proteins data was obtained and kept compressed in .gz format to reduce space used.  This is mostly because the .cif files have a lot of unecessary information.  So if this rcsb protein database is used the protein cif files would likely be requested in batches of 1000 and deleted after obtaining the relevant information.  For example, to predict protein secondary structure the protein amino acid sequence after "_pdbx_poly_seq_scheme.hetero" would be obtained.  Then, the alpha helix locations under "_struct_conf.pdbx_PDB_helix_length" and beta sheet locations under "_struct_sheet_range.end_auth_seq_id" would also be stored.  


batch_download.sh: used to download protein cif files if protein id is in list_file.txt with command:
./batch_download.sh -f list_file.txt -c

entry_ids.txt: List of all 227933 protein ids obtained from https://data.rcsb.org/rest/v1/holdings/current/entry_ids .

id_splitter.py: Reads "entry_ids.txt" and inserts the first 15,000 ids into "0_5000_entry_ids.txt", "5000_10000_entry_ids.txt", and "10000_15000_entry_ids.txt" respectively.

0_5000_entry_ids.txt: has first 5000 protein ids from entry_ids.txt.  Used with batch_download to inside 0_5000_entry_ids to locate 5000 cif files there.

0_5000_entry_ids: folder with 5000 cif files compressed in .gz format.

5000_10000_entry_ids.txt: has the protein ids' [5000,10000) from entry_ids.txt.  Used with batch_download to inside 5000_10000_entry_ids to locate 5000 cif files there.

5000_10000_entry_ids: folder with 5000 cif files compressed in .gz format.

10000_15000_entry_ids.txt: has the protein ids' [10000,15000) from entry_ids.txt.  Used with batch_download to inside 10000_15000_entry_ids to locate 5000 cif files there.

10000_15000_entry_ids: folder with 5000 cif files compressed in .gz format.

1AS8.cif: folder with the exported .gz file for the cif file of the protein with id 1AS8.  Example of the format which doesn't require downloading a .gz and exporting it yourself.



