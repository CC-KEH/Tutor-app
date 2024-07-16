import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:quiz/Router/configuration.dart';

// Screens
import 'package:quiz/screens/register.dart';
import 'package:quiz/screens/createsubject.dart';
import 'package:quiz/screens/profile.dart';
import 'package:quiz/screens/quiz.dart';
import 'package:quiz/screens/settings.dart';
import 'package:quiz/screens/subjects.dart';
import 'package:quiz/screens/welcome.dart';
import 'package:quiz/Screens/LoginScreen.dart';

void main(){
  runApp(MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      routerConfig: custom_router,
    );
  }
}
