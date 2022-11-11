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

    @GetMapping("/listar")
    public List<Permiso> listarPermiso(){
        return this.miRepoPermiso.findAll();
    }


    @PostMapping("/crear")
    public Permiso crearPermiso(@RequestBody Permiso permisoEntrada){
        return this.miRepoPermiso.save(permisoEntrada);
    }


    @DeleteMapping("/eliminar/{idPermiso}")
    public String eliminarPermiso(@PathVariable String idPermiso){
        miRepoPermiso.deleteById(idPermiso);
        return "se ha eliminado el permiso con el id: "+ idPermiso;
    }

    @PutMapping("/actualizar/{idPermiso}")
    public String actualizarPermiso (@PathVariable String idPermiso,@RequestBody Permiso permisoEntrada){
        Permiso permisoBusqueda = miRepoPermiso.findById(idPermiso).orElse(null);
        permisoBusqueda.setUrl(permisoEntrada.getUrl());
        permisoBusqueda.setMetodo(permisoEntrada.getMetodo());
        miRepoPermiso.save(permisoBusqueda);
        return "El permiso con id: "+ idPermiso + " fue actualizado";

    }

}
