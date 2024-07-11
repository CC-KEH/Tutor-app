import 'dart:ui';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/painting.dart';
import 'package:flutter/rendering.dart';
import 'package:quiz/constants.dart';

class SubjectsScreen extends StatelessWidget {
  const SubjectsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    const int no = 1;
    int subject_count = 0;
    return Material(
      child: Container(
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.height,
        color: white_color,
        child: Stack(
          children: [
            Column(
              children: [
                Container(
                  width: MediaQuery.of(context).size.width,
                  decoration: const BoxDecoration(
                    color: white_color,
                  ),
                  child: Column(
                    children: [
                      const SizedBox(height: 40),
                      const Padding(
                        padding: EdgeInsets.symmetric(horizontal: 15),
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Icon(Icons.arrow_back_rounded,size: 35,),
                            Text(
                              'My Subjects',
                              style: TextStyle(
                                color: Colors.black,
                                fontSize: 35,
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                            Icon(Icons.settings,size: 35,),
                          ],
                        ),
                      ),
                      if (subject_count > 0)
                        Container(
                          height: MediaQuery.of(context).size.height / 1.2,
                          width: MediaQuery.of(context).size.width / 1.02,
                          child: GridView.count(
                            crossAxisCount: 2,
                            scrollDirection: Axis.vertical,
                            children: List.generate(subject_count, (index) {
                              return Container(
                                margin:
                                    const EdgeInsets.all(8), // Updated margin
                                child: Center(
                                  child: Container(
                                    width: MediaQuery.of(context).size.width /
                                        2.5, // Adjusted width
                                    height: MediaQuery.of(context).size.width /
                                        2, // Adjusted height
                                    decoration: BoxDecoration(
                                      color: option_color,
                                      borderRadius: BorderRadius.circular(20),
                                    ),
                                    child: Padding(
                                      padding: const EdgeInsets.all(20.0),
                                      child: Text(
                                        'Subject ${index + 1}',
                                        style: const TextStyle(
                                          color: Colors.black,
                                          fontSize: 20,
                                        ),
                                      ),
                                    ),
                                  ),
                                ),
                              );
                            }),
                          ),
                        )
                      else
                        Column(
                          children: [
                            const SizedBox(
                              height: 50,
                            ),
                            Image.asset(
                              'assets/books.jpg',
                            ),
                            const Text(
                              'You have not added any Subjects yet.',
                              style: TextStyle(
                                  fontSize: 20, color: Colors.black54),
                            )
                          ],
                        ),
                    ],
                  ),
                ),
              ],
            ),
            Positioned(
              bottom: 30,
              right: 25,
              child: Padding(
                padding: const EdgeInsets.all(8.0),
                child: CircleAvatar(
                  radius: 35,
                  backgroundColor: selected_button_color,
                  child: Center(
                    child: IconButton(
                      onPressed: () {},
                      icon: const Icon(
                        Icons.add,
                        size: 50,
                      ),
                    ),
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
