-- CREATE DATABASE stme_wes_db;


-- 测序批次
DROP TABLE IF EXISTS wes_sequencing_batch;
CREATE TABLE wes_sequencing_batch(
    id SERIAL NOT NULL,
    batch_name VARCHAR(900),
    sequencing_working_set VARCHAR(255),
    sequencing_instrument VARCHAR(255),
    sequencing_output VARCHAR(900),
    q30 INTEGER,
    qc VARCHAR(255),
    qc_positive VARCHAR(32),
    qc_ntc VARCHAR(32),
    completion_time TIMESTAMP,
    reviewer_id INTEGER,
    reviewer_time TIMESTAMP,
    review_status TIMESTAMP,
    review_result VARCHAR(32),
    created_by VARCHAR(32),
    created_time TIMESTAMP,
    updated_by VARCHAR(32),
    updated_time TIMESTAMP,
    PRIMARY KEY (id)
);

COMMENT ON TABLE wes_sequencing_batch IS '测序批次';
COMMENT ON COLUMN wes_sequencing_batch.id IS 'id';
COMMENT ON COLUMN wes_sequencing_batch.batch_name IS '批次名称';
COMMENT ON COLUMN wes_sequencing_batch.sequencing_working_set IS '测序工作集';
COMMENT ON COLUMN wes_sequencing_batch.sequencing_instrument IS '测序仪器';
COMMENT ON COLUMN wes_sequencing_batch.sequencing_output IS '测序产出';
COMMENT ON COLUMN wes_sequencing_batch.q30 IS 'Q30百分比';
COMMENT ON COLUMN wes_sequencing_batch.qc IS 'QC质控';
COMMENT ON COLUMN wes_sequencing_batch.qc_positive IS 'positive质控';
COMMENT ON COLUMN wes_sequencing_batch.qc_ntc IS 'NTC质控';
COMMENT ON COLUMN wes_sequencing_batch.completion_time IS '完成时间';
COMMENT ON COLUMN wes_sequencing_batch.reviewer_id IS '审阅人';
COMMENT ON COLUMN wes_sequencing_batch.reviewer_time IS '审阅时间';
COMMENT ON COLUMN wes_sequencing_batch.review_status IS '审阅状态';
COMMENT ON COLUMN wes_sequencing_batch.review_result IS '审阅结果';
COMMENT ON COLUMN wes_sequencing_batch.created_by IS '创建人';
COMMENT ON COLUMN wes_sequencing_batch.created_time IS '创建时间';
COMMENT ON COLUMN wes_sequencing_batch.updated_by IS '更新人';
COMMENT ON COLUMN wes_sequencing_batch.updated_time IS '更新时间';


-- 样本管理
DROP TABLE IF EXISTS wes_sequencing_sample;
CREATE TABLE wes_sequencing_sample(
    id SERIAL NOT NULL,
    sample_id VARCHAR(32),
    batch_id VARCHAR(32),
    batch_name VARCHAR(255),
    lab_code VARCHAR(255),
    test_item VARCHAR(32),
    sample_type VARCHAR(32),
    acession_type VARCHAR(32),
    sequencing_output VARCHAR(900),
    alignable_percentage INTEGER,
    sequencing_depth_avg INTEGER,
    q30 INTEGER,
    qc_batch VARCHAR(32),
    qc_sample VARCHAR(32),
    completion_time TIMESTAMP,
    reviewer_id INTEGER,
    reviewer_time TIMESTAMP,
    review_status TIMESTAMP,
    review_result VARCHAR(32),
    created_by VARCHAR(32),
    created_time TIMESTAMP,
    updated_by VARCHAR(32),
    updated_time TIMESTAMP,
    PRIMARY KEY (id)
);

COMMENT ON TABLE wes_sequencing_sample IS '样本';
COMMENT ON COLUMN wes_sequencing_sample.id IS 'id';
COMMENT ON COLUMN wes_sequencing_sample.sample_id IS '样本编号';
COMMENT ON COLUMN wes_sequencing_sample.batch_id IS '批次ID';
COMMENT ON COLUMN wes_sequencing_sample.batch_name IS '批次名称';
COMMENT ON COLUMN wes_sequencing_sample.lab_code IS '实验室代码';
COMMENT ON COLUMN wes_sequencing_sample.test_item IS '检测项目';
COMMENT ON COLUMN wes_sequencing_sample.sample_type IS '样本类型';
COMMENT ON COLUMN wes_sequencing_sample.acession_type IS 'acession类型';
COMMENT ON COLUMN wes_sequencing_sample.sequencing_output IS '测序产出';
COMMENT ON COLUMN wes_sequencing_sample.alignable_percentage IS '可比对百分比';
COMMENT ON COLUMN wes_sequencing_sample.sequencing_depth_avg IS '平均测序深度';
COMMENT ON COLUMN wes_sequencing_sample.q30 IS 'Q30百分比';
COMMENT ON COLUMN wes_sequencing_sample.qc_batch IS '批次QC';
COMMENT ON COLUMN wes_sequencing_sample.qc_sample IS '样本QC';
COMMENT ON COLUMN wes_sequencing_sample.completion_time IS '完成时间(签发报告时间)';
COMMENT ON COLUMN wes_sequencing_sample.reviewer_id IS '审阅人';
COMMENT ON COLUMN wes_sequencing_sample.reviewer_time IS '审阅时间';
COMMENT ON COLUMN wes_sequencing_sample.review_status IS '审阅状态';
COMMENT ON COLUMN wes_sequencing_sample.review_result IS '审阅结果';
COMMENT ON COLUMN wes_sequencing_sample.created_by IS '创建人';
COMMENT ON COLUMN wes_sequencing_sample.created_time IS '创建时间';
COMMENT ON COLUMN wes_sequencing_sample.updated_by IS '更新人';
COMMENT ON COLUMN wes_sequencing_sample.updated_time IS '更新时间';

-- 基因突变

DROP TABLE IF EXISTS wes_sequencing_gene_mutation;
CREATE TABLE wes_sequencing_gene_mutation(
    id SERIAL NOT NULL,
    batch_id VARCHAR(32),
    sample_id VARCHAR(32),
    gene_name VARCHAR(255),
    transcript VARCHAR(255),
    chromosomal_location VARCHAR(255),
    ref VARCHAR(32),
    alt VARCHAR(32),
    snv_or_cnv VARCHAR(32),
    hgvs_gene VARCHAR(255),
    hgvs_protein VARCHAR(255),
    mutation_frequency NUMERIC(24,6),
    ad_or_dp VARCHAR(255),
    qual INTEGER,
    mutation_structural_types VARCHAR(255),
    mutation_functional_types VARCHAR(255),
    exon_or_intron VARCHAR(255),
    dbsnp_id VARCHAR(255),
    population_frequency_gnomad VARCHAR(255),
    functional_prediction VARCHAR(255),
    genetic_pattern VARCHAR(32),
    mutation_origin VARCHAR(32),
    phenotype_chpo VARCHAR(255),
    phenotype_score NUMERIC(24,6),
    db_omim VARCHAR(255),
    db_disease VARCHAR(255),
    db_ophanet VARCHAR(255),
    clinvar VARCHAR(255),
    pathogenicity_evidence_level VARCHAR(255),
    final_related_disease VARCHAR(255),
    clinical_interpretation_info VARCHAR(255),
    final_pathogenicity_determination VARCHAR(255),
    result_classfiy VARCHAR(255),
    is_report VARCHAR(255),
    reviewer_id INTEGER,
    reviewer_time TIMESTAMP,
    review_status TIMESTAMP,
    review_result VARCHAR(32),
    created_by VARCHAR(32),
    created_time TIMESTAMP,
    updated_by VARCHAR(32),
    updated_time TIMESTAMP,
    PRIMARY KEY (id)
);

COMMENT ON TABLE wes_sequencing_gene_mutation IS '基因突变';
COMMENT ON COLUMN wes_sequencing_gene_mutation.id IS 'id';
COMMENT ON COLUMN wes_sequencing_gene_mutation.batch_id IS '批次编号';
COMMENT ON COLUMN wes_sequencing_gene_mutation.sample_id IS '样本编号';
COMMENT ON COLUMN wes_sequencing_gene_mutation.gene_name IS '基因名称';
COMMENT ON COLUMN wes_sequencing_gene_mutation.transcript IS '转录本';
COMMENT ON COLUMN wes_sequencing_gene_mutation.chromosomal_location IS '染色体位置';
COMMENT ON COLUMN wes_sequencing_gene_mutation.ref IS 'ref';
COMMENT ON COLUMN wes_sequencing_gene_mutation.alt IS 'alt';
COMMENT ON COLUMN wes_sequencing_gene_mutation.snv_or_cnv IS 'snv/cnv';
COMMENT ON COLUMN wes_sequencing_gene_mutation.hgvs_gene IS 'HGVS基因命名';
COMMENT ON COLUMN wes_sequencing_gene_mutation.hgvs_protein IS 'HGVS蛋白命名';
COMMENT ON COLUMN wes_sequencing_gene_mutation.mutation_frequency IS '突变频率';
COMMENT ON COLUMN wes_sequencing_gene_mutation.ad_or_dp IS 'AD/DP';
COMMENT ON COLUMN wes_sequencing_gene_mutation.qual IS 'QUAL';
COMMENT ON COLUMN wes_sequencing_gene_mutation.mutation_structural_types IS '突变结构类型';
COMMENT ON COLUMN wes_sequencing_gene_mutation.mutation_functional_types IS '突变功能类型';
COMMENT ON COLUMN wes_sequencing_gene_mutation.exon_or_intron IS '外显子/内含子';
COMMENT ON COLUMN wes_sequencing_gene_mutation.dbsnp_id IS 'dbSNP ID';
COMMENT ON COLUMN wes_sequencing_gene_mutation.population_frequency_gnomad IS '人群频率(Gnomad)';
COMMENT ON COLUMN wes_sequencing_gene_mutation.functional_prediction IS '功能预测';
COMMENT ON COLUMN wes_sequencing_gene_mutation.genetic_pattern IS '遗传模式';
COMMENT ON COLUMN wes_sequencing_gene_mutation.mutation_origin IS '突变来源';
COMMENT ON COLUMN wes_sequencing_gene_mutation.phenotype_chpo IS 'CHPO表型';
COMMENT ON COLUMN wes_sequencing_gene_mutation.phenotype_score IS '表型打分';
COMMENT ON COLUMN wes_sequencing_gene_mutation.db_omim IS '相关疾病数据库（OMIM）';
COMMENT ON COLUMN wes_sequencing_gene_mutation.db_disease IS '相关疾病数据库()';
COMMENT ON COLUMN wes_sequencing_gene_mutation.db_ophanet IS '相关疾病数据库（Ophanet）';
COMMENT ON COLUMN wes_sequencing_gene_mutation.clinvar IS 'Clinvar';
COMMENT ON COLUMN wes_sequencing_gene_mutation.pathogenicity_evidence_level IS '致病性证据等级（ClinGen)';
COMMENT ON COLUMN wes_sequencing_gene_mutation.final_related_disease IS '最终关联疾病';
COMMENT ON COLUMN wes_sequencing_gene_mutation.clinical_interpretation_info IS '临床解读信息';
COMMENT ON COLUMN wes_sequencing_gene_mutation.final_pathogenicity_determination IS '最终致病性判断（根据ACMG等级去判断）';
COMMENT ON COLUMN wes_sequencing_gene_mutation.result_classfiy IS '结果分类';
COMMENT ON COLUMN wes_sequencing_gene_mutation.is_report IS '是否报告';
COMMENT ON COLUMN wes_sequencing_gene_mutation.reviewer_id IS '审阅人';
COMMENT ON COLUMN wes_sequencing_gene_mutation.reviewer_time IS '审阅时间';
COMMENT ON COLUMN wes_sequencing_gene_mutation.review_status IS '审阅状态';
COMMENT ON COLUMN wes_sequencing_gene_mutation.review_result IS '审阅结果';
COMMENT ON COLUMN wes_sequencing_gene_mutation.created_by IS '创建人';
COMMENT ON COLUMN wes_sequencing_gene_mutation.created_time IS '创建时间';
COMMENT ON COLUMN wes_sequencing_gene_mutation.updated_by IS '更新人';
COMMENT ON COLUMN wes_sequencing_gene_mutation.updated_time IS '更新时间';

-- 报告

DROP TABLE IF EXISTS wes_sequencing_report;
CREATE TABLE wes_sequencing_report(
    id SERIAL NOT NULL,
    sample_id VARCHAR(255),
    lab_code VARCHAR(255),
    test_item VARCHAR(32),
    sample_type VARCHAR(32),
    acession_type VARCHAR(32),
    completion_time TIMESTAMP,
    reviewer_id INTEGER,
    reviewer_time TIMESTAMP,
    review_status TIMESTAMP,
    review_result VARCHAR(32),
    conclusion VARCHAR(255),
    is_issued VARCHAR(255),
    created_by VARCHAR(32),
    created_time TIMESTAMP,
    updated_by VARCHAR(32),
    updated_time TIMESTAMP,
    PRIMARY KEY (id)
);

COMMENT ON TABLE wes_sequencing_report IS '报告';
COMMENT ON COLUMN wes_sequencing_report.id IS 'id';
COMMENT ON COLUMN wes_sequencing_report.sample_id IS '批次编号';
COMMENT ON COLUMN wes_sequencing_report.lab_code IS '实验室代码';
COMMENT ON COLUMN wes_sequencing_report.test_item IS '检测项目';
COMMENT ON COLUMN wes_sequencing_report.sample_type IS '样本类型';
COMMENT ON COLUMN wes_sequencing_report.acession_type IS 'acession类型';
COMMENT ON COLUMN wes_sequencing_report.completion_time IS '完成时间(签发报告时间)';
COMMENT ON COLUMN wes_sequencing_report.reviewer_id IS '审阅人';
COMMENT ON COLUMN wes_sequencing_report.reviewer_time IS '审阅时间';
COMMENT ON COLUMN wes_sequencing_report.review_status IS '审阅状态';
COMMENT ON COLUMN wes_sequencing_report.review_result IS '审阅结果';
COMMENT ON COLUMN wes_sequencing_report.conclusion IS '报告结论';
COMMENT ON COLUMN wes_sequencing_report.is_issued IS '报告签发';
COMMENT ON COLUMN wes_sequencing_report.created_by IS '创建人';
COMMENT ON COLUMN wes_sequencing_report.created_time IS '创建时间';
COMMENT ON COLUMN wes_sequencing_report.updated_by IS '更新人';
COMMENT ON COLUMN wes_sequencing_report.updated_time IS '更新时间';

-- 注释数据库
DROP TABLE IF EXISTS wes_annotation_db;
CREATE TABLE wes_annotation_db(
    id SERIAL NOT NULL,
    disease_name VARCHAR(255),
    genetic_pattern VARCHAR(32),
    gene_name VARCHAR(255),
    mutation_cds VARCHAR(255),
    disease_description VARCHAR(255),
    omim_id VARCHAR(255),
    mutation_description VARCHAR(255),
    created_by VARCHAR(32),
    created_time TIMESTAMP,
    updated_by VARCHAR(32),
    updated_time TIMESTAMP,
    PRIMARY KEY (id)
);

COMMENT ON TABLE wes_annotation_db IS '注释数据库';
COMMENT ON COLUMN wes_annotation_db.id IS 'id';
COMMENT ON COLUMN wes_annotation_db.disease_name IS '疾病名称';
COMMENT ON COLUMN wes_annotation_db.genetic_pattern IS '遗传模式';
COMMENT ON COLUMN wes_annotation_db.gene_name IS '基因名称';
COMMENT ON COLUMN wes_annotation_db.mutation_cds IS 'CDS基因突变';
COMMENT ON COLUMN wes_annotation_db.disease_description IS '疾病描述';
COMMENT ON COLUMN wes_annotation_db.omim_id IS 'OMIM编号';
COMMENT ON COLUMN wes_annotation_db.mutation_description IS '突变说明';
COMMENT ON COLUMN wes_annotation_db.created_by IS '创建人';
COMMENT ON COLUMN wes_annotation_db.created_time IS '创建时间';
COMMENT ON COLUMN wes_annotation_db.updated_by IS '更新人';
COMMENT ON COLUMN wes_annotation_db.updated_time IS '更新时间';


-- 批次原始数据

DROP TABLE IF EXISTS wes_sequencing_origin_data;
CREATE TABLE wes_sequencing_origin_data(
    id SERIAL NOT NULL,
    raw VARCHAR(900),
    batch_id VARCHAR(255),
    batch_status VARCHAR(255),
    created_by VARCHAR(32),
    created_time TIMESTAMP,
    updated_by VARCHAR(32),
    updated_time TIMESTAMP,
    PRIMARY KEY (id)
);

COMMENT ON TABLE wes_sequencing_origin_data IS '批次原始数据';
COMMENT ON COLUMN wes_sequencing_origin_data.id IS 'id';
COMMENT ON COLUMN wes_sequencing_origin_data.raw IS '原始数据json';
COMMENT ON COLUMN wes_sequencing_origin_data.batch_id IS '批次编号';
COMMENT ON COLUMN wes_sequencing_origin_data.batch_status IS '处理状态[未生成批次，已生成批次]';
COMMENT ON COLUMN wes_sequencing_origin_data.created_by IS '创建人';
COMMENT ON COLUMN wes_sequencing_origin_data.created_time IS '创建时间';
COMMENT ON COLUMN wes_sequencing_origin_data.updated_by IS '更新人';
COMMENT ON COLUMN wes_sequencing_origin_data.updated_time IS '更新时间';
