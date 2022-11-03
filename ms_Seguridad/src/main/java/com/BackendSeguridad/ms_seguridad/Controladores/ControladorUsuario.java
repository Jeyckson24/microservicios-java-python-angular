package com.BackendSeguridad.ms_seguridad.Controladores;

import com.BackendSeguridad.ms_seguridad.Modelos.Usuario;
import com.BackendSeguridad.ms_seguridad.Repositorios.RepositorioUsuario;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/user")
public class ControladorUsuario {
    @Autowired
    private RepositorioUsuario miRepositorio;
    @GetMapping("/listar")
    public List<Usuario> listar(){
        return miRepositorio.findAll();
    }
    @PostMapping("/crear")
    public Usuario crearUsuario(@RequestBody Usuario usuarioEntrada){
        return miRepositorio.save(usuarioEntrada);
    }
    @DeleteMapping("/eliminar")
    public String eliminarUsuario(String idUsuario){
        miRepositorio.deleteById(idUsuario);
       return "Usuario" + idUsuario + "eliminado";
    }



}
