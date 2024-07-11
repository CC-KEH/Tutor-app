import 'package:quiz/model/model.dart';

class Data {
  static List<Category> categories = [
    Category(
      name: 'Course 1',
      image: 'assets/book.jpg',
      quizSets: [
        QuizSet(
          name: 'Easy',
          questions: [
            Question(
              'What is Flutter?',
              [
                'A UI framework',
                'A programming language',
                'An operating system',
                'None of the above'
              ],
              0,
            ),
            Question(
              'What language is Flutter written in?',
              ['Dart', 'Java', 'Kotlin', 'C++'],
              0,
            ),
            Question(
              'What is hot reload in Flutter?',
              [
                'A feature for quickly seeing changes in code',
                'A widget',
                'A plugin',
                'None of the above'
              ],
              0,
            ),
            Question(
              'Which widget is used to display images in Flutter?',
              ['Image', 'ImageView', 'ImageBox', 'ImageDisplay'],
              0,
            ),
            Question(
              'What is the purpose of MaterialApp widget in Flutter?',
              [
                'To create a Material Design app',
                'To define app theme',
                'To handle app routing',
                'None of the above'
              ],
              0,
            ),
            Question(
              'What is a StatefulWidget in Flutter?',
              [
                'A widget with mutable state',
                'A static widget',
                'A stateless widget',
                'None of the above'
              ],
              0,
            ),
            Question(
              'What is the purpose of setState() method in Flutter?',
              [
                'To update the state of a StatefulWidget',
                'To build the UI',
                'To navigate to another screen',
                'None of the above'
              ],
              0,
            ),
            Question(
              'What is the purpose of Scaffold widget in Flutter?',
              [
                'To implement basic material design layout structure',
                'To handle user input',
                'To display images',
                'None of the above'
              ],
              0,
            ),
            Question(
              'What is the main function in Flutter?',
              [
                'Entry point of the app',
                'To define app theme',
                'To define app routing',
                'None of the above'
              ],
              0,
            ),
            Question(
              'What is the purpose of pubspec.yaml file in Flutter project?',
              [
                'To define project dependencies',
                'To define UI layout',
                'To define app theme',
                'None of the above'
              ],
              0,
            ),
          ],
        ),
        QuizSet(
          name: 'Medium',
          questions: [
            Question(
              'What is a widget in Flutter?',
              [
                'A building block of the user interface',
                'A programming language',
                'A UI framework',
                'None of the above'
              ],
              0,
            ),
            Question(
              'What is the purpose of StatelessWidget in Flutter?',
              [
                'To represent immutable UI',
                'To handle user input',
                'To manage app state',
                'None of the above'
              ],
              0,
            ),
            Question(
              'What is the difference between hot reload and hot restart in Flutter?',
              [
                'Hot reload updates the UI without restarting the app',
                'Hot restart restarts the app',
                'They are the same',
                'None of the above'
              ],
              0,
            ),
            Question(
              'What is the purpose of the Material class in Flutter?',
              [
                'To implement Material Design',
                'To define app theme',
                'To manage app routing',
                'None of the above'
              ],
              0,
            ),
            Question(
              'What is the purpose of Cupertino widgets in Flutter?',
              [
                'To implement iOS-style UI',
                'To handle user input',
                'To display images',
                'None of the above'
              ],
              0,
            ),
          ],
        ),
        // Add more quiz sets for Flutter
      ],
    ),
    Category(
      name: 'Course 2',
      image: 'assets/book.jpg',
      quizSets: [
        QuizSet(
          name: 'Easy',
          questions: [
            // Add questions for Quiz Set 1 of React Native
          ],
        ),
        QuizSet(
          name: 'Medium',
          questions: [
            // Add questions for Quiz Set 2 of React Native
          ],
        ),
        QuizSet(
          name: 'Hard',
          questions: [
            // Add questions for Quiz Set 3 of React Native
          ],
        ),
      ],
    ),
    Category(
      name: 'Course 3',
      image: 'assets/book.jpg',
      quizSets: [
        QuizSet(
          name: 'Easy',
          questions: [
            // Add questions for Quiz Set 1 of Python
          ],
        ),
        QuizSet(
          name: 'Medium',
          questions: [
            // Add questions for Quiz Set 2 of Python
          ],
        ),
        QuizSet(
          name: 'Hard',
          questions: [
            // Add questions for Quiz Set 3 of Python
          ],
        ),
      ],
    ),
    // Add more categories with quiz sets and questions
    Category(
      name: 'Course 4',
      image: 'assets/book.jpg',
      quizSets: [
        QuizSet(
          name: 'Easy',
          questions: [
            // Add questions for Quiz Set 1 of Python
          ],
        ),
        QuizSet(
          name: 'Medium',
          questions: [
            // Add questions for Quiz Set 2 of Python
          ],
        ),
        QuizSet(
          name: 'Hard',
          questions: [
            // Add questions for Quiz Set 3 of Python
          ],
        ),
      ],
    ),
    // Add more categories with quiz sets and questions


  ];
}
