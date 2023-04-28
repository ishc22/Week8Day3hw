# Using the skills we covered in class, update the Flask application to have a create user route and get user route. You should have the following routes:

@api.route('/users/<user.id>')
    def get(user_id):
    user = User.query.filter.get(user.id, user)
    if user is None:
        return {'error' f'User does not exist.'}, 404
    return user.dict()


@api.route('/users', methoids='POST')
    def create_user():
    if not request.is_json:
        return {'error' f'Your request is not JSON'}
    data = request.json()
    required_fields = [first_name, last_name, email, password, username]
    missing_fields = []
    for field in required_fields:
        if field not in data:
             missing_fields.append(field)
    if missing_fields:
        return(error,: f"{','join(missing_fields)} must be in request body"), 400
    first = data.get('first_name')
    last = data.get('last_name')
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    check_user = User.query.filter((User.username == username) | (User.email == email)).all()
    if check_user:
        return {'error': 'User with that username and/or email already exists'}, 400
    new_user = User(first_name=first, last_name=last, email=email, username=username, password=password)
    return new_user.to_dict(), 201

    

