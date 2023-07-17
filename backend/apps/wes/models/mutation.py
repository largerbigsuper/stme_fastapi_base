import datetime
from sqlalchemy import Column, DateTime, Integer, String, Numeric, TIMESTAMP

from core.db.session import Base

class Mutation(Base):
    __tablename__ = 'wes_sequencing_mutation'
    __table_args__ = {'comment': '突变'}

    id = Column(Integer, primary_key=True, comment='id')
    batch_id = Column(String(32), comment='批次编号')
    sample_id = Column(String(32), comment='样本编号')
    gene_name = Column(String(255), comment='基因名称')
    transcript = Column(String(255), comment='转录本')
    chromosomal_location = Column(String(255), comment='染色体位置')
    ref = Column(String(32), comment='ref')
    alt = Column(String(32), comment='alt')
    snv_or_cnv = Column(String(32), comment='snv/cnv')
    hgvs_gene = Column(String(255), comment='HGVS基因命名')
    hgvs_protein = Column(String(255), comment='HGVS蛋白命名')
    mutation_frequency = Column(Numeric(24,6), comment='突变频率')
    ad_or_dp = Column(String(255), comment='AD/DP')
    qual = Column(Integer, comment='QUAL')
    mutation_structural_types = Column(String(255), comment='突变结构类型')
    mutation_functional_types = Column(String(255), comment='突变功能类型')
    exon_or_intron = Column(String(255), comment='外显子/内含子')
    dbsnp_id = Column(String(255), comment='dbSNP ID')
    population_frequency_gnomad = Column(String(255), comment='人群频率(Gnomad)')
    functional_prediction = Column(String(255), comment='功能预测')
    genetic_pattern = Column(String(32), comment='遗传模式')
    mutation_origin = Column(String(32), comment='突变来源')
    phenotype_chpo = Column(String(255), comment='CHPO表型')
    phenotype_score = Column(Numeric(24,6), comment='表型打分')
    db_omim = Column(String(255), comment='相关疾病数据库（OMIM）')
    db_disease = Column(String(255), comment='相关疾病数据库()')
    db_ophanet = Column(String(255), comment='相关疾病数据库（Ophanet）')
    clinvar = Column(String(255), comment='Clinvar')
    pathogenicity_evidence_level = Column(String(255), comment='致病性证据等级（ClinGen)')
    final_related_disease = Column(String(255), comment='最终关联疾病')
    clinical_interpretation_info = Column(String(255), comment='临床解读信息')
    final_pathogenicity_determination = Column(String(255), comment='最终致病性判断（根据ACMG等级去判断）')
    result_classfiy = Column(String(255), comment='结果分类')
    is_report = Column(String(255), comment='是否报告')
    reviewer_id = Column(Integer, comment='审阅人')
    reviewer_time = Column(DateTime(timezone=True), comment='审阅时间')
    review_status = Column(String(120), comment='审阅状态')
    review_result = Column(String(32), comment='审阅结果')
    created_by = Column(String(32), comment='创建人')
    created_time = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, comment='创建时间')
    updated_by = Column(String(32), comment='更新人')
    updated_time = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow, comment='更新时间')

