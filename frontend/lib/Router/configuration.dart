import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:quiz/Screens/LoginScreen.dart';
import 'package:quiz/Screens/profile.dart';
import 'package:quiz/screens/register.dart';
import 'package:quiz/screens/createsubject.dart';
import 'package:quiz/screens/quiz.dart';
import 'package:quiz/screens/subjects.dart';
import 'package:quiz/screens/welcome.dart';

final GoRouter _router = GoRouter(
  routes: <RouteBase>[
    GoRoute(
      name: 'main_page',
      path: '/',
      builder: (BuildContext context, GoRouterState state) {
        return const WelcomeScreen();
      },
      routes: <RouteBase>[
        GoRoute(
          path: 'register',
          builder: (BuildContext context, GoRouterState state) {
            return const RegistrationScreen();
          },
        ),
        GoRoute(
          path: 'login',
          builder: (BuildContext context, GoRouterState state) {
            return const LoginScreen();
          },
        ),
        GoRoute(
            path: 'subjects',
            builder: (BuildContext context, GoRouterState state) {
              return SubjectsScreen();
            },
            routes: [
              GoRoute(
                path: 'create_subject',
                builder: (BuildContext context, GoRouterState state) {
                  return CreateSubjectScreen();
                },
              ),
              GoRoute(
                path: 'quiz/:topic',
                builder: (BuildContext context, GoRouterState state) {
                  return QuizScreen(topic: state.pathParameters['topic'],);
                },
              ),
            ]
        ),
        GoRoute(
          path: 'settings',
          builder: (BuildContext context, GoRouterState state) {
            return const SubjectsScreen();
          },
        ),
        GoRoute(
          path: 'profile',
          builder: (BuildContext context, GoRouterState state) {
            return const ProfileScreen();
          },
        ),
      ],
    ),
  ],
);