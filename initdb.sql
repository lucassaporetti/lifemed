CREATE TABLE IF NOT EXISTS patient_tb (
    uuid VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255),
    birth_date DATE,
    phones VARCHAR(255),
    plan_linked BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS plan_tb (
    uuid VARCHAR(36) PRIMARY KEY,
    description VARCHAR(255),
    phones VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS specialty_tb (
    uuid VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS doctor_tb (
    uuid VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255),
    crm VARCHAR(255),
    specialty_id VARCHAR(36),
    FOREIGN KEY (specialty_id) REFERENCES specialty_tb(uuid)
);

CREATE TABLE IF NOT EXISTS procedure_tb (
    uuid VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255),
    value FLOAT
);

CREATE TABLE IF NOT EXISTS plan_contract_tb (
    uuid VARCHAR(36) PRIMARY KEY,
    patient_id VARCHAR(36),
    plan_contract VARCHAR(255),
    plan_id VARCHAR(36),
    FOREIGN KEY (patient_id) REFERENCES patient_tb(uuid),
    FOREIGN KEY (plan_id) REFERENCES plan_tb(uuid)
);

CREATE TABLE IF NOT EXISTS appointment_tb (
    uuid VARCHAR(36) PRIMARY KEY,
    patient_id VARCHAR(36),
    doctor_id VARCHAR(36),
    datetime TIMESTAMP,
    private BOOLEAN NOT NULL,
    procedure_id VARCHAR(36),
    plan_contract_id VARCHAR(36),
    FOREIGN KEY (patient_id) REFERENCES patient_tb(uuid),
    FOREIGN KEY (doctor_id) REFERENCES doctor_tb(uuid),
    FOREIGN KEY (procedure_id) REFERENCES procedure_tb(uuid),
    FOREIGN KEY (plan_contract_id) REFERENCES plan_contract_tb(uuid)
);