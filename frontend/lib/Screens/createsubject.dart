import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/painting.dart';
import 'package:flutter/widgets.dart';
import 'package:quiz/constants.dart';

class CreateSubjectScreen extends StatelessWidget {
  const CreateSubjectScreen({super.key});

  @override
  Widget build(BuildContext context) {
    const int no = 1;
    return Material(
      child: Column(
        children: [
          const SizedBox(
            height: 40,
          ),
          const Padding(
            padding: EdgeInsets.symmetric(horizontal: 15),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Icon(
                  Icons.arrow_back_rounded,
                  size: 35,
                ),
                Text(
                  'Create Subject',
                  style: TextStyle(
                    color: Colors.black,
                    fontSize: 35,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                Icon(
                  Icons.settings,
                  size: 35,
                ),
              ],
            ),
          ),
          Form(
              child: Column(
            children: [
              const SizedBox(height: 50,),
              const Text(
                'Enter the subject details',
                style: TextStyle(fontSize: 20),
              ),
              const Padding(
                padding: EdgeInsets.symmetric(vertical: 40, horizontal: 20),
                child: TextField(
                  decoration: InputDecoration(
                      border: OutlineInputBorder(), labelText: 'Name'),
                ),
              ),
              const Padding(
                padding: EdgeInsets.symmetric(vertical: 0, horizontal: 20),
                child: TextField(
                  decoration: InputDecoration(
                      border: OutlineInputBorder(), labelText: 'Description'),
                ),
              ),
              const Padding(
                padding: EdgeInsets.symmetric(vertical: 40, horizontal: 20),
                child: TextField(
                  decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Important Topics'),
                ),
              ),
              Padding(
                padding:
                    const EdgeInsets.symmetric(vertical: 0, horizontal: 20),
                child: GestureDetector(
                  child: Container(
                    width: MediaQuery.of(context).size.width / 2,
                    height: 50,
                    decoration:
                         BoxDecoration(color: option_color,borderRadius: BorderRadius.circular(20)),
                    child: const Padding(
                      padding: EdgeInsets.symmetric(vertical: 13),
                      child: Text(
                        textAlign: TextAlign.center,
                        'Upload Documents',
                        style: TextStyle(fontSize: 15),
                      ),
                    ),
                  ),
                ),
              ),
              const SizedBox(height: 50,),
              GestureDetector(
                child: Container(
                  width: MediaQuery.of(context).size.width / 2,
                  height: 50,
                  decoration:
                  BoxDecoration(color: option_color,borderRadius: BorderRadius.circular(20)),
                  child: const Padding(
                    padding: EdgeInsets.symmetric(vertical: 13),
                    child: Text(
                      textAlign: TextAlign.center,
                      'Save Subject',
                      style: TextStyle(fontSize: 15),
                    ),
                  ),
                ),
              ),
            ],
          )),
        ],
      ),
    );
  }
}
