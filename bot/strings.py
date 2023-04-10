import os

STRINGS = {
    'start_msg': 'Choose an option🔽 ',
    'number_of_users_btn': f'Number of Users: {os.getenv("NUMBER_OF_USERS")}',
    'max_posts_per_user_btn': f'Max Posts per User: {os.getenv("MAX_POSTS_PER_USER")}',
    'max_likes_per_user_btn': f'Max Likes per User: {os.getenv("MAX_LIKE_PER_USER")}',
    'read_config_btn': 'Read Configs🛠',
    'signup_user_btn': 'Signup User💁‍♂️',
    'create_random_posts_btn': 'Create Random Posts🎲',
    'random_likes_btn': 'Like Random Posts👍',
}
