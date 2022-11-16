package com.BackendSeguridad.ms_seguridad.Controladores;


import com.BackendSeguridad.ms_seguridad.Modelos.Permiso;
import com.BackendSeguridad.ms_seguridad.Modelos.Rol;
import com.BackendSeguridad.ms_seguridad.Modelos.RolPermiso;
import com.BackendSeguridad.ms_seguridad.Repositorios.RepositorioPermiso;
import com.BackendSeguridad.ms_seguridad.Repositorios.RepositorioRol;
import com.BackendSeguridad.ms_seguridad.Repositorios.RepositorioRolPermiso;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RequestMapping("/rolpermiso")
@RestController

public class ControladorRolPermiso {
    @Autowired
    RepositorioRolPermiso _repositorio_rol_permiso;
    @Autowired
    RepositorioRol _repositorio_rol;
    @Autowired
    RepositorioPermiso _repositorio_permiso;

    @GetMapping("")
    public List <RolPermiso> listarRolPermiso(){
        return _repositorio_rol_permiso.findAll();

    }
    @PostMapping("/{idRol}/{idPermiso}")
    public RolPermiso  crearRolPermiso(@PathVariable String idRol, @PathVariable String idPermiso){

        Rol rolConsulta = _repositorio_rol.findById(idRol).orElse(null);
        Permiso permisoConsulta = _repositorio_permiso.findById(idPermiso).orElse(null);
        RolPermiso rolPermiso = new RolPermiso(rolConsulta,permisoConsulta);
        return _repositorio_rol_permiso.save(rolPermiso);

    }
    @DeleteMapping("{idRolPermiso}")
    public String eliminarRolPermiso(@PathVariable String idRolPermiso){
        _repositorio_rol_permiso.deleteById(idRolPermiso);
        return "Se elimino el permiso asignado";

    }
    @PutMapping("/{idRolpermiso}/{idRol}/{idPermiso}")
    public String  actualizarRolPermiso(@PathVariable String idRolPermiso, @PathVariable String idRol, @PathVariable String idPermiso){

        Rol rolConsulta = _repositorio_rol.findById(idRol).orElse(null);
        Permiso permisoConsulta = _repositorio_permiso.findById(idPermiso).orElse(null);
        RolPermiso rolPermiso = new RolPermiso(rolConsulta, permisoConsulta);
        rolPermiso.setRol(rolConsulta);
        rolPermiso.setPermiso(permisoConsulta);
        _repositorio_rol_permiso.save(rolPermiso);
        return "se ha actualizado el permiso del perfil";

    }
}
