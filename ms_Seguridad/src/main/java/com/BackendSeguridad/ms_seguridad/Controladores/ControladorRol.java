package com.BackendSeguridad.ms_seguridad.Controladores;

import com.BackendSeguridad.ms_seguridad.Modelos.Rol;
import com.BackendSeguridad.ms_seguridad.Repositorios.RepositorioRol;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
@CrossOrigin
@RestController
@RequestMapping("/rol")
public class ControladorRol {
    @Autowired
    private RepositorioRol miRepoRol;

    @GetMapping("/listar")
    public List<Rol> listar(){
        return miRepoRol.findAll();
    }

    @PostMapping("/crear")
    public Rol crearRol(@RequestBody Rol rolEntrada){
        return miRepoRol.save(rolEntrada);
    }

    @DeleteMapping("/eliminar")
    public String eliminarRol(@RequestParam(value = "idRol") String _idRol){
        miRepoRol.deleteById(_idRol);
        return "Rol " + _idRol + " eliminado";
    }

}
