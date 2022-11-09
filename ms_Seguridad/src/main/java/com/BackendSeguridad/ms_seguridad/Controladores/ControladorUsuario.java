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
    @DeleteMapping("/{idUsuario}")
    public String eliminarUsuario(@PathVariable String idUsuario){
        miRepositorio.deleteById(idUsuario);
       return "Usuario" + idUsuario + "eliminado";
    }

    @PutMapping ("/{idUsuario}")
    public String actualizarUsuario(@PathVariable String idUsuario, @RequestBody Usuario usuarioEntrada){
        Usuario usuarioBusqueda = miRepositorio.findById(idUsuario).orElse(null);
        usuarioBusqueda.setNombre_usuario(usuarioEntrada.getNombre_usuario());
        usuarioBusqueda.setContrasena(usuarioEntrada.getContrasena());
        usuarioBusqueda.setCorreo(usuarioEntrada.getCorreo());
        miRepositorio.save(usuarioBusqueda);
        return "Usuario" + idUsuario + "actualizado";
    }



}
