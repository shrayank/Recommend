from common import *

# input -> NULL
def add_constraint_userID(*args):
    script_name = "add_constraint_userID.cql"
    output = execute_neo4j_shell(script_name, *args)
    return output

# input -> NULL
def add_constraint_movieID(*args):
    script_name = "add_constraint_movieID.cql"
    output = execute_neo4j_shell(script_name, *args)
    return output

# input -> (userID)
def is_userID_present(*args):
    script_name = "is_userID_present.cql"
    output = execute_neo4j_shell(script_name, *args)
    ret = output.splitlines()[3][2] is '0'
    return not ret

# input -> (movieID)
def is_movieID_present(*args):
    script_name = "is_movieID_present.cql"
    output = execute_neo4j_shell(script_name, *args)
    ret = output.splitlines()[3][2] is '0'
    return not ret

# input -> NULL
def show_movies(*args):
    script_name = "show_movies.cql"
    output = execute_neo4j_shell(script_name, *args)
    return output

# input -> (userID)
def show_ratings(*args):
    script_name = "show_ratings.cql"
    output = execute_neo4j_shell(script_name, *args)
    return output

# input -> (userID, movieID, rating)
def update_rating(*args):
    script_name = "update_rating.cql"
    output = execute_neo4j_shell(script_name, *args)
    return output

# input -> (userID)
def compute_similarity(*args):
    script_name = "compute_similarity.cql"
    output = execute_neo4j_shell(script_name, *args)
    return output

# input -> (userID)
def get_recommendations(*args):
    compute_similarity(*args)
    script_name = "get_recommendations.cql"
    output = execute_neo4j_shell(script_name, *args)
    return output


add_constraint_userID()
add_constraint_movieID()