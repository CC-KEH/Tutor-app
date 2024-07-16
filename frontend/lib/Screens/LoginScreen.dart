import 'dart:ui';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/painting.dart';
import 'package:flutter/rendering.dart';
import 'package:go_router/go_router.dart';
import 'package:quiz/Router/constants.dart';
import 'package:quiz/constants.dart';
import 'package:quiz/utils.dart';


class LoginScreen extends StatelessWidget {

  const LoginScreen({super.key});
  @override
  Widget build(BuildContext context) {
    bool is_autheticated = false;
    return Material(
      color: white_color,
      child: Column(
        children: [
          const SizedBox(
            height: 40,
          ),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 15),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                GestureDetector(
                  onTap: (){
                    GoRouter.of(context).pop();
                  },
                  child: const Icon(
                    Icons.arrow_back_rounded,
                    size: 35,
                  ),
                ),
                const Text(
                  'Login',
                  style: TextStyle(
                    color: Colors.black,
                    fontSize: 35,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                GestureDetector(
                  onTap: (){
                    GoRouter.of(context).pushNamed(MyAppRouteConstants.settings);
                  },
                  child: const Icon(
                    Icons.settings,
                    size: 35,
                  ),
                ),
              ],
            ),
          ),
          Form(
            child: Column(
              children: [
                const SizedBox(height: 40),
                 Container(
                  width: MediaQuery.of(context).size.width,
                  height: MediaQuery.of(context).size.height / 2.5,
                  child: Image.asset(
                    'assets/writing.jpg',
                  ),
                ),
                const SizedBox(
                  height: 50,
                ),
                const Padding(
                  padding: EdgeInsets.symmetric(vertical: 0, horizontal: 20),
                  child: TextField(
                    decoration: InputDecoration(
                        border: OutlineInputBorder(
                          borderSide: BorderSide(
                            color: option_color,
                          ),
                        ),
                        focusedBorder: OutlineInputBorder(
                          borderSide: BorderSide(
                              color: selected_button_color, width: 2),
                        ),
                        errorBorder: OutlineInputBorder(
                          borderSide: BorderSide(color: Colors.red, width: 2),
                        ),
                        labelText: 'Email',
                        labelStyle: TextStyle(color: Colors.black)),
                  ),
                ),
                const Padding(
                  padding: EdgeInsets.symmetric(vertical: 20, horizontal: 20),
                  child: TextField(
                    decoration: InputDecoration(
                        border: OutlineInputBorder(
                            borderSide: BorderSide(color: option_color)),
                        focusedBorder: OutlineInputBorder(
                          borderSide: BorderSide(
                              color: selected_button_color, width: 2),
                        ),
                        errorBorder: OutlineInputBorder(
                          borderSide: BorderSide(color: Colors.red, width: 2),
                        ),
                        labelText: 'Password',
                        labelStyle: TextStyle(color: Colors.black)),
                  ),
                ),
                Padding(
                  padding:
                      const EdgeInsets.symmetric(vertical: 10, horizontal: 20),
                  child: MouseRegion(
                    cursor: SystemMouseCursors.click,
                    child: GestureDetector(
                      onTap: (){
                        is_autheticated = authenticate_user();
                        if (is_autheticated){
                          GoRouter.of(context).pushNamed(MyAppRouteConstants.profile);
                        }
                      },
                      child: Container(
                        width: MediaQuery.of(context).size.width / 3,
                        height: 50,
                        decoration: BoxDecoration(
                            color: option_color,
                            borderRadius: BorderRadius.circular(20)),
                        child: const Padding(
                          padding: EdgeInsets.symmetric(vertical: 13),
                          child: Text(
                            textAlign: TextAlign.center,
                            'Login',
                            style: TextStyle(fontSize: 15),
                          ),
                        ),
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
