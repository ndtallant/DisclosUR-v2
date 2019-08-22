echo .exit | sqlite3 --init scripts/create_db.sql web/app.db
echo .exit | sqlite3 --init scripts/clean_db.sql web/app.db
