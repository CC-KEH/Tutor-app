import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:quiz/Router/constants.dart';
import 'package:quiz/Screens/LoginScreen.dart';
import 'package:quiz/Screens/error_screen.dart';
import 'package:quiz/Screens/profile.dart';
import 'package:quiz/Screens/settings.dart';
import 'package:quiz/screens/register.dart';
import 'package:quiz/screens/createsubject.dart';
import 'package:quiz/screens/quiz.dart';
import 'package:quiz/screens/subjects.dart';
import 'package:quiz/screens/welcome.dart';

final custom_router = GoRouter(
  initialLocation: '/',
  routes: [
    GoRoute(
      name: MyAppRouteConstants.main,
      path: '/',
      builder: (context, state) => const WelcomeScreen(),
    ),
    GoRoute(
      name: MyAppRouteConstants.register,
      path: '/register',
      builder: (context, state) => const RegistrationScreen(),
    ),
    GoRoute(
      name: MyAppRouteConstants.login,
      path: '/login',
      builder: (context, state) => const LoginScreen(),
    ),
    GoRoute(
        name: MyAppRouteConstants.subjects,
        path: '/subjects',
        builder: (context, state) => const SubjectsScreen(),
    ),
    GoRoute(
        name: MyAppRouteConstants.create_subject,
        path: '/create_subject',
        builder: (context, state) => const CreateSubjectScreen(),
    ),
    GoRoute(
      name: MyAppRouteConstants.settings,
      path: '/settings',
      builder: (context, state) => const SettingsScreen(),
    ),
    GoRoute(
      name: MyAppRouteConstants.profile,
      path: '/profile',
      builder: (context, state) => const ProfileScreen(),
    ),
  ],
  errorBuilder: (context, state) => const ErrorScreen(),
);
