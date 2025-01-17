import 'package:sqflite/sqflite.dart';

class MockExamCache {
  static final MockExamCache instance = MockExamCache._privateConstructor();
  static Database? _database;
  static const String _tableName = "questions";

  MockExamCache._privateConstructor();

  Future<Database> get database async {
    if (_database != null) {
      return _database!;
    }
    _database = await _initDatabase();
    return _database!;
  }

  Future<Database> _initDatabase() async {
    final String path = '${await getDatabasesPath()}mock_exam.db';
    return await openDatabase(
      path,
      version: 1,
      onCreate: _createTable,
    );
  }

  Future<void> _createTable(Database db, int version) async {
    await db.execute("""
      CREATE TABLE $_tableName ( 
        id TEXT PRIMARY KEY, 
        area TEXT,
        statement TEXT, 
        alternatives TEXT,
        answer TEXT,
        is_essay BOOLEAN,
        rating INTEGER,
        answered TEXT,
        duration INTEGER
      )
    """);
  }

  Future<void> insert(Map<String, dynamic> question) async {
    final db = await database;
    await db.insert(_tableName, question,
        conflictAlgorithm: ConflictAlgorithm.replace);
  }

  Future<void> update(Map<String, dynamic> question) async {
    final db = await database;
    final id = question['id'];
    await db.update(
      _tableName,
      question,
      where: 'id = ?',
      whereArgs: [id],
    );
  }

  Future<void> deleteTable() async {
    final db = await database;
    await db.delete(_tableName);
  }

  Future<bool> doesTableExists(Database db, String tableName) async {
    List<Map<String, dynamic>> tables =
        await db.rawQuery("SELECT name FROM sqlite_master WHERE type='table'");

    return tables.any((table) => table['name'] == tableName);
  }
}
