package com.BackendSeguridad.ms_seguridad.Controladores;

import com.BackendSeguridad.ms_seguridad.Modelos.Permiso;
import com.BackendSeguridad.ms_seguridad.Repositorios.RepositorioPermiso;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/permisos")
public class ControladorPermiso {
    @Autowired
    private RepositorioPermiso miRepoPermiso;

    @PostMapping("/crear")
    public Permiso crearPermiso(@RequestBody Permiso permisoEntrada){
        return this.miRepoPermiso.save(permisoEntrada);
    }

    @GetMapping("/listar")
    public List<Permiso> listarPermiso(){
        return this.miRepoPermiso.findAll();
    }

    @DeleteMapping("/eliminar")
    public String eliminarPermiso(String idPermiso){
        miRepoPermiso.deleteById(idPermiso);
        return "se ha eliminado el permiso con el codigo"+ idPermiso;
    }
}
