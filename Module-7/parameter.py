#Programmer Mohymin Islam
#Date of creation: 6/19/2022
#Purpose: This parameter will deliver database query IPYNB file.


## rescue type : water
water={'$and': [
            {'$or': [{'breed': 'Labrador Retriever Mix'}, {'breed': 'Chesapeake Bay Retriever'},
                     {'breed': 'Newfoundland'}]},
            {'sex_upon_outcome': 'Intact Female'}, {"age_upon_outcome_in_weeks":{"$gte":26},"age_upon_outcome_in_weeks":{"$lte":156}}]}

#resucue type : Mountain or Wilderness
mountain={'$and': [
            {'$or': [ {'breed':'German Shepherd'}, {'breed':'Alaskan Malamute'},
                   {'breed':'Old English Sheepdog'},{'breed':'Siberian Husky'},{'breed':'Rottweiler'}]},
            {'sex_upon_outcome':'Intact Male'}, {"age_upon_outcome_in_weeks":{"$gte":26},"age_upon_outcome_in_weeks":{"$lte":156}}]}

#rescue type : Disaster or Individual Tracking
disaster={'$and': [
            {'$or': [ {'breed':'Doberman Pinscher'}, {'breed':'German Sheperd'},
                   {'breed':'Golden Retriever'},{'breed':'Bloodhound'},{'breed':'Rottweiler'}]},
            {'sex_upon_outcome':'Intact Male'}, {"age_upon_outcome_in_weeks":{"$gte":20},"age_upon_outcome_in_weeks":{"$lte":300}}]}
