package com.BackendSeguridad.ms_seguridad.Controladores;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ControladorUsuario {
    @GetMapping("/usuarios")
    public String listar(){
        return "lista de usuarios";
    }
}
