package com.example.pythonapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.DeadObjectException;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;


import com.chaquo.python.Kwarg;
import com.chaquo.python.PyObject;
import com.chaquo.python.android.AndroidPlatform;
import com.chaquo.python.Python;



public class MainActivity extends AppCompatActivity {
    private TextView text0;
    private Button button;
    private Button button2;
    private Button button3;
    private Button button4;

    @Override

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        text0 = (TextView)findViewById(R.id.text0);
        button = (Button)findViewById(R.id.button);
        button2 = (Button)findViewById(R.id.button2);
        button3 = (Button) findViewById(R.id.button3);
        button4 = (Button) findViewById(R.id.button4);

        if (! Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }
        Python py = Python.getInstance();

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

            }
        });

        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String wav_path = "";

                PyObject obj1 = py.getModule("get_result").callAttr("get_result", wav_path);

                Integer result = obj1.toJava(Integer.class);

                text0.setText("Result: 第"+result+"类疾病");

            }
        });

        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String wav_path = "";

                PyObject obj1 = py.getModule("get_period").callAttr("get_period", wav_path);

                Double result = obj1.toJava(Double.class);

                text0.setText("Result: "+result+"ms");

            }
        });

        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

            }
        });


    }
}