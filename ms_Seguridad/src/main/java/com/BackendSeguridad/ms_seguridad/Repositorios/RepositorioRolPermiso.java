package com.BackendSeguridad.ms_seguridad.Repositorios;

import com.BackendSeguridad.ms_seguridad.Modelos.RolPermiso;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioRolPermiso extends MongoRepository<RolPermiso,String> {
}
