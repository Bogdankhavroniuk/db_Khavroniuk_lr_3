DO $$
 DECLARE 
   S_I INT;
   P_i INT ;


 BEGIN
     S_I :=108 ;
     P_i :=8;
      WHILE(@P_I <= 14)
	  
	   LOOP
	      INSERT INTO player (player_id )
			  VALUES (P_i );
		  INSERT INTO statistic (stat_id, player_id)
			 VALUES (S_I  , P_i );
	 

		  S_i  = @S_i + 1 ; 
		  P_i  = @P_i +1 ;
		 
			
	    END LOOP;
 END;
 $$
 
 
