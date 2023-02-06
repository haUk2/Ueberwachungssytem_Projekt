import 'package:flutter/material.dart';
import 'package:email_passwort_login/config/palette.dart';

class ButtonWidget extends StatelessWidget {
  final IconData icon;
  final String text;
  final VoidCallback onClicked;

  const ButtonWidget({
    Key? key,
    required this.icon,
    required this.text,
    required this.onClicked,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) => ElevatedButton(
        
        
        
        style: ElevatedButton.styleFrom(
          elevation: 5,
          primary: Palette.purpleaccent2,
          minimumSize: const Size.fromHeight(50),
        ),
        child: buildContent(),
        onPressed: onClicked,
      );

  Widget buildContent() => Row(
        
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(icon, size: 24, color: Colors.white),
          const SizedBox(width: 15),
          Text(
            text,
            style: const TextStyle(fontSize: 20, color: Colors.white, fontWeight: FontWeight.w800),
          ),
        ],
      );
}
