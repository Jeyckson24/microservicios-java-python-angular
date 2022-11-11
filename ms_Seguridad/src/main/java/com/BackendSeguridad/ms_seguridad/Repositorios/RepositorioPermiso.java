package com.BackendSeguridad.ms_seguridad.Repositorios;

import com.BackendSeguridad.ms_seguridad.Modelos.Permiso;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioPermiso extends MongoRepository <Permiso,String> {


}
