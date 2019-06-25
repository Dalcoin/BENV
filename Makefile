all: eb_server_v3.f eb_v3.f
	f90 $$F90FLAGS -o xeb_server -s -w eb_v3.f eb_server_v3.f $$LINK_FNL

exec: eb_run_box.f eb.f
	f90 $$F90FLAGS -o exec -s -w eb.f eb_run_box.f $$LINK_FNL

	
clean:
	rm -f exec xeb_server values.out values_min.out eb check
	
	
	
	
	
	
