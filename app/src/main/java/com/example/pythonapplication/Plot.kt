package com.example.pythonapplication

import android.content.Context
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.os.Bundle
import android.view.inputmethod.InputMethodManager
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.chaquo.python.PyException
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform


class Plot {

    fun CreatePlot(): ByteArray {
        val py =Python.getInstance()
        val model =py.getModule("plot")
        val bytes = model.callAttr("plot").toJava(ByteArray::class.java)
        return bytes;
    }

}