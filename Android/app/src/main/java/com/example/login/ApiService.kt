package com.example.login

import retrofit2.http.GET

// Definimos el objeto que esperamos recibir a partir de lo que se manda desde FastAPI
data class WelcomeResponse(val message: String)

interface ApiService {
    @GET("/") // Apunta a la raíz del servidor
    suspend fun getWelcomeMessage(): WelcomeResponse
}
