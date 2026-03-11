package com.example.login

import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import kotlinx.coroutines.launch
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val txtResponse = findViewById<TextView>(R.id.txtResponse)

        // Configurar Retrofit
        val retrofit = Retrofit.Builder()
            .baseUrl("http://10.0.2.2:8000/")
            .addConverterFactory(GsonConverterFactory.create())
            .build()

        val apiService = retrofit.create(ApiService::class.java)

        // Ejecutar la petición en un hilo secundario
        lifecycleScope.launch {
            try {
                val response = apiService.getWelcomeMessage()
                // Actualizamos la UI con el mensaje del servidor
                txtResponse.text = response.message
            } catch (e: Exception) {
                // Si el servidor está apagado o no hay internet
                txtResponse.text = "Error: No se pudo conectar al backend"
                e.printStackTrace()
            }
        }
    }
}
